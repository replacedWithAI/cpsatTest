from typing import Any
from Data_types.Course import Course
from Data_types.Sections import Section
from Data_types.Lecture import Lecture
from ortools.sat.python import cp_model

class CPSAT_variable_maker: # I am so sorry, there's so much nesting. Hopefully you learnt HTML?
    def __time_to_index(start_time: str) -> int: # sum all units of time into one numerical value
        hour = start_time[:2]
        minutes = start_time[3:]
        return hour*60 + minutes


    def __create_start_time_variables(self, courses: list[Course]) -> dict[dict[dict[dict, Any]]]:
        model = cp_model.CpModel
        
        start_time_variables = {
            course: {
                section: {

                    {other_class_session: {
                        class_session_start_time: model.new_int_var_from_domain(
                                cp_model.Domain_from_intervals
                                (
                                    self.__time_to_index
                                        (class_session_start_time)
                                ), 

                                f"start_{other_class_session.activity_name}_from_" +
                                f"{course.department + course.course_code}_section_{section.letter}"
                            )
                        for class_session_start_time in other_class_session.start_times
                        }
                    for other_class_session in (section.lectures.other_class_sessions)},

                    {section.lectures: model.new_int_var_from_domain(
                        cp_model.Domain_from_intervals
                        (
                            self.__time_to_index
                                (section.lectures.start_times)
                        ),
                        f"start_lecture_from_{course.department + course.course_code}_section_{section.letter}"
                    )}
                }
                for section in course.sections
            }
            for course in courses
        }
            
        return start_time_variables
        
        

    def __create_is_present_variables(self, courses: list[Course]) -> list[dict[str, dict[dict, Any]]]:
        # will need to check session for SU or FW
        model = cp_model.CpModel
        semester_1 = {"M": [], "T": [], "W": [], "R": [], "F": []}
        semester_2 = {"M": [], "T": [], "W": [], "R": [], "F": []}
        both_semesters_flag = False
        num_repeats = 1

        for course in courses:
            course_name = course.department + " " + course.course_code
            for section in course.sections:
                if section.term == 'F' or 'S1':
                    curr_semester = semester_1
                elif section.term == 'W' or 'S2':
                    curr_semester = semester_2
                elif section.term == 'Y' or 'SU':
                    both_semesters_flag = True
                    num_repeats = 2
                    curr_semester = semester_1

                lecture = section.lectures
                lecture_days = lecture.days

                for j in range(num_repeats):

                    for i in range(len(lecture_days)):
                        curr_semester[lecture_days[i]].append(
                            {course: {
                                {section: model.new_bool_var(f"{course_name}_section_{section.letter}")}
                            }}
                        )

                    if both_semesters_flag is True:
                        curr_semester = semester_2
                        if j is 1:
                            curr_semester = semester_1
                        

                other_class_sessions = lecture.other_class_sessions

                for other_class_session in other_class_sessions:
                    other_class_session_days = other_class_session.days

                    for j in range(num_repeats):
                        
                        for i in range(len(other_class_session_days)):
                            curr_semester[lecture_days[i]].append(
                            {course: {
                                {section: model.new_bool_var(f"{course_name}_section_{section.letter}")}
                            }}
                        )
                            
                        if both_semesters_flag is True:
                            curr_semester = semester_2
                            if j is 1:
                                curr_semester = semester_1

        return [semester_1, semester_2]


    def __create_interval_variables(self, start_time_variables, is_present_variables):
        return

    def __init__(self, courses):
        self.start_time_variables = self.__create_start_time_variables(courses)
        self.is_present_variables = self.__create_is_present_variables(courses)
        
