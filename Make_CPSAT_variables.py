from typing import Any
from Course import Course
from Sections import Sections
from Lecture import Lecture
from ortools.sat.python import cp_model

class CPSAT_variable_maker:
    def __time_to_index(start_time: str) -> int: # sum all units of time into one numerical value
        hour = start_time[:2]
        minutes = start_time[3:]
        return hour*60 + minutes

    def __iterate_through_courses_sections(self, courses: list[Course]):
        start_time_variable = []
        for course in courses:
            for section in course.sections:
                lecture = section.lectures

                for other_class_session in lecture.other_class_sessions:
                course_name
                self.__create_CPSAT_variables(course_name, section_name, section)
                    
    def __add_lectures_and_other_class_sessions(self, course_name: str, section_name: str, section: Sections):
        # will add basic conditions/constraints for timetabling in another class

        start_times_variable = {
            course_name: {
                section_name: {
                    
                }
            }
        }

        def __create_start_time_variables(self, courses: list[Course]):
            model = cp_model.CpModel

            start_time_variables = {
                course.course_name: {
                    section.section_letter: {

                        {other_class_sessions: model.new_int_var_from_domain(
                            cp_model.Domain_from_intervals(other_class_sessions.start_times), 
                            f"start_{other_class_sessions.activity_name}"
                        )
                        for other_class_sessions in section.lectures},

                        {section.lectures: model.new_int_var_from_domain(
                            cp_model.Domain_from_intervals(section.lectures.start_times),
                            f"start_lecture_{section.lectures.activity_name}"
                        )}
                    }
                    for section in course.Sections
                }
                for course in courses
            }
                
            return start_time_variables


        def __create_is_present_variables():
    

    def __init__(self):
