from lib.Data_types.Course import Course
from lib.Data_types.Sections import Section
from lib.Data_types.Lecture import Lecture
from typing import Any
from ortools.sat.python import cp_model

class Start_time_variable_maker:
    def __init__(self, courses):
        self.start_time_variables = self.__create_start_time_variables(courses)


    def __create_start_time_variables(self, courses: list[Course]) -> \
                                                     dict[Section, list[Any]]:        
        start_time_variables = {
            course: {
                section: self.__classes_start_times(section.lectures, 
                                                    (course.department + " " 
                                                     + course.course_code), 
                                                    section.section_letter)
                for section in course.sections
            }
            for course in courses
        }
            
        return start_time_variables
    

    def __classes_start_times(self, lecture: Lecture, course_name: str, 
                              section_letter: str) -> list[Any]:
        model = cp_model.CpModel
        classes = []

        for i in range(len(lecture.global_start_times)):
            start_time_variable = model.new_int_var(lecture.global_start_times[i],
                                                    lecture.global_end_times[i],
                                                    f"{course_name}_section_ \
                                                      {section_letter}_lecture_start")
            classes.append(start_time_variable)

        for other_class in lecture.other_class_sessions:

            for i in range(len(other_class.global_start_times)):
                start_time_variable = model.new_int_var(other_class.global_start_times[i],
                                                        other_class.global_end_times[i],
                                                        f"{course_name}_section_ \
                                                          {section_letter}_\
                                                          {other_class.activity_name[i]} \
                                                          _start")
            classes.append(start_time_variable)

        return classes
