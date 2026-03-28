from Group_intervals_by_day import group_intervals_by_day
from lib.Data_types.Course import Course
from lib.Data_types.Class_sessions import Class_session
from typing import Any
from ortools.sat.python import cp_model

class Constraint_adder:
    def __init__(self,
                 is_present_variables: dict[dict[dict[int, Any]]], 
                 interval_variables: dict[dict[dict[int, Any]]], 
                 courses: list[Course], 
                 model: cp_model):
        
        self.__add_no_overlap_constraint(interval_variables, courses, model)

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
                curr_section_presence = is_present_variables[course_name] \
                                                         [section_letter] \
                                                         [classes[0]] \
                                                         [0]
                sections_available.append(curr_section_presence)

                self.__add_one_lab_tutorial_per_section(is_present_variables,
                                                        curr_section_presence, 
                                                        course_name, 
                                                        section_letter, 
                                                        classes, 
                                                        model)
                
        
    def __add_one_lab_tutorial_per_section(self,
                                           is_present_variables: dict[dict[dict[int, Any]]], 
                                           curr_section_presence: Any, 
                                           course_name: str, 
                                           section_letter: str, 
                                           classes: list[Class_session], 
                                           model: cp_model):
        chooseable_classes = [[]]
        unique_chooseable_class = 0 # suppose can choose from 5 labs, 3 tutorials

        for i in range(len(classes)):
            for j in range(len(classes[i].start_times)):

                curr_is_present_variable = is_present_variables[course_name] \
                                                               [section_letter] \
                                                               [classes[i].activity_name] \
                                                               [j]
                
                is_chooseable_class = (curr_section_presence != curr_is_present_variable)
                if (is_chooseable_class):
                    chooseable_classes[unique_chooseable_class].append(
                                                        curr_is_present_variable)
                    
                    next_chooseable_class_is_unique = (i+1 != len(classes) and \
                                                      "01" in classes[i+1].activity_name)
                    if (next_chooseable_class_is_unique):
                        num_unique_chooseable_classes += 1
                        chooseable_classes.append([])

        for i in range(len(chooseable_classes)):
            model.add(sum(chooseable_classes[i]) == curr_section_presence)
                


    def __add_no_overlap_constraint(self, 
                                    interval_variables: dict[dict[dict[int, Any]]], 
                                    courses: list[Course], 
                                    model: cp_model):
        
        for course in courses:
            for section in course.sections:
                for curr_class in section.classes:
                    for interval in (interval_variables[course.course_name]
                                                       [section.section_letter]
                                                       [curr_class.activity_name]):
                        model.add_no_overlap(interval)
        return
    
    