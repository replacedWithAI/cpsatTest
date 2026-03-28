from lib.Data_types.Course import Course
from lib.Data_types.Class_sessions import Class_session
from typing import Any
from ortools.sat.python import cp_model
import operator as op 
def __add_one_section_per_course(self, 
                                is_present_variables: dict[dict[dict[int, Any]]], 
                                courses: list[Course], 
                                model: cp_model):
    for course in courses:
        course_name = course.department + " " + course.course_code
        model.add(sum(sections_available) == 1)

        for section in course.sections:
            sections_available = []
            section_letter = section_letter
            classes = section.classes

            # each section has a lecture; use lecture's presence variable
            curr_section_taken = is_present_variables[course_name] \
                                                     [section_letter] \
                                                     [classes[0]] \
                                                     [0]
            sections_available.append(curr_section_taken)

            self.__add_one_lab_tutorial_per_section(is_present_variables,
                                                    curr_section_taken, 
                                                    course_name, 
                                                    section_letter, 
                                                    classes, 
                                                    model)
        

def __add_one_lab_tutorial_per_section(self,
                                    is_present_variables: dict[dict[dict[int, Any]]], 
                                    curr_section_taken: Any, 
                                    course_name: str, 
                                    section_letter: str, 
                                    classes: list[Class_session], 
                                    model: cp_model):
    


        

        

