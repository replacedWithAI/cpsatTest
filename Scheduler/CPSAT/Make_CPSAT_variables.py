from typing import Any
from Scheduler.lib.Data_types.Course import Course
from Scheduler.lib.Data_types.Sections import Section
from Scheduler.lib.Data_types.Class_sessions import Class_session
from ortools.sat.python import cp_model

# might want to put this in lib, but that's for a while later
class CPSAT_variable_maker: # I am so sorry, there's so much nesting. Hopefully you learnt HTML?
    def __init__(self, courses, model):
        self.start_time_variables = self.__create_start_time_variables(courses)
        self.is_present_variables = self.__create_is_present_variables(courses, model)
        self.interval_variables = self.__create_interval_variables(self.start_time_variables, \
                                                                   self.is_present_variables, \
                                                                   courses, \
                                                                   model)

    def __create_start_time_variables(self, courses: list[Course]) -> \
                                                     dict[dict[str, list[Any]]]:        
        start_time_variables = {
            course.course_name: {
                section.section_letter: self.__classes_start_times(section.classes, \
                                                    (course.department + "_" 
                                                     + course.course_code), \
                                                    section.section_letter)
                for section in course.sections
            }
            for course in courses
        }
            
        return start_time_variables
    

    def __classes_start_times(self, classes, 
                              course_name: str, 
                              section_letter: str) -> list[Any]:
        curr_start_time = {
            curr_class.activity_name: {
                i: curr_class.global_start_times[i]
                for i in range(len(classes.start_time))
            }
            for curr_class in classes
        } 

        return classes
    

    def __create_is_present_variables(self, courses: list[Course], 
                                      model: cp_model) \
                                      -> dict[dict[str, list[Any]]]:
        is_present_variables = {
            course.course_name: {
                section.section_letter: self.__classes_is_present(section.classes, \
                                                   (course.department + "_"
                                                     + course.course_code), \
                                                    section.section_letter, 
                                                    model)
                for section in course.sections
            }
            for course in courses
        }

        return is_present_variables
    
    
    def __classes_is_present(self, 
                             classes: list[Class_session], 
                             course_name: str, \
                             section_letter: str, 
                             model: cp_model) -> list[Any]:
        curr_is_present = {
            curr_class.activity_name: {
                i: model.new_bool_var(f"{course_name}_section_" + \
                                      f"{section_letter}_" + \
                                      f"{curr_class.activity_name}" + \
                                      f"_taken")
                for i in range(len(classes.start_time))
            
            }
            for curr_class in classes
        } 

        return curr_is_present
    
    def __create_interval_variables(self,
                                    start_time_variables: dict[dict[str, list[Any]]],
                                    is_present_variables: dict[dict[str, list[Any]]],
                                    courses: list[Course], \
                                    model: cp_model) \
                                    -> dict[dict[str, list[Any]]]:
        
        interval_variables = {
            course.course_name: {
                section.section_letter: self.__classes_intervals
                                        ( \
                                            start_time_variables[course.course_name][section.section_letter], \
                                            is_present_variables[course.course_name][section.section_letter],\
                                            course.course_name,\
                                            section.section_letter, \
                                            section.classes, \
                                            model
                                        )

                for section in course.sections
            }
            for course in courses
        }

        return interval_variables


    def __classes_intervals(self, \
                            start_time_variables: list[Any], \
                            is_present_variables: list[Any], \
                            course_name:str, \
                            section_letter:str, \
                            classes: list[Class_session], \
                            model: cp_model)-> list[Any]:
        
        curr_interval = {
            curr_class.activity_name: {
                i: model.new_optional_fixed_size_interval_var(
                            start = start_time_variables[i], \
                            size = curr_class.durations[i], \
                            is_present = is_present_variables[i], \
                            name = f"{course_name}_section_{section_letter}_" \
                                + f"lecture_interval" \
                            )
                for i in range(len(curr_class.start_time))
            }
            for curr_class in classes
        }
        
        return curr_interval