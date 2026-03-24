from typing import Any
from Scheduler.lib.Data_types.Course import Course
from Scheduler.lib.Data_types.Sections import Section
from Scheduler.lib.Data_types.Lecture import Lecture
from ortools.sat.python import cp_model

# might want to put this in lib, but that's for a while later
class CPSAT_variable_maker: # I am so sorry, there's so much nesting. Hopefully you learnt HTML?
    def __init__(self, courses):
        self.start_time_variables = self.__create_start_time_variables(courses)
        self.is_present_variables = self.__create_is_present_variables(courses)
        self.interval_variables = self.__create_interval_variables(self.start_time_variables, \
                                                                   self.is_present_variables, \
                                                                   courses)

    def __create_start_time_variables(self, courses: list[Course]) -> \
                                                     dict[dict[str, list[Any]]]:        
        start_time_variables = {
            course.course_name: {
                section.section_letter: self.__classes_start_times(section.lectures, \
                                                    (course.department + "_" 
                                                     + course.course_code), \
                                                    section.section_letter)
                for section in course.sections
            }
            for course in courses
        }
            
        return start_time_variables
    

    def __classes_start_times(self, lecture: Lecture, course_name: str, 
                                section_letter: str) -> list[Any]:
        classes = []

        for i in range(len(lecture.global_start_times)):
            start_time_variable = lecture.global_start_times[i]
            classes.append(start_time_variable)

        for other_class in lecture.other_class_sessions:
            for i in range(len(other_class.global_start_times)):

                start_time_variable = other_class.global_start_times[i]
            classes.append(start_time_variable)

        return classes
    

    def __create_is_present_variables(self, courses: list[Course]) -> \
                                        dict[dict[str, list[Any]]]:
        is_present_variables = {
            course.course_name: {
                section.section_letter: self.__classes_is_present(section.lectures, \
                                                   (course.department + "_"
                                                     + course.course_code), \
                                                    section.section_letter)
                for section in course.sections
            }
            for course in courses
        }

        return is_present_variables
    
    
    def __classes_is_present(self, lecture: Lecture, course_name: str, \
                             section_letter: str) -> list[Any]:
        model = cp_model.CpModel()
        classes = []

        for i in range(len(lecture.global_start_times)):
            is_present_variable = model.new_bool_var(name = f"{course_name}_section_" + \
                                                            f"{section_letter}_lecture_taken")
            classes.append(is_present_variable)

        for other_class in lecture.other_class_sessions:
            for i in range(len(other_class.global_start_times)):

                is_present_variable = model.new_bool_var(name = f"{course_name}_section_" + \
                                                                f"{section_letter}_" + \
                                                                f"{other_class.activity_name}" + \
                                                                f"_taken")
                classes.append(is_present_variable)

        return classes
    
    def __create_interval_variables(self,
                                    start_time_variables: dict[dict[str, list[Any]]],
                                    is_present_variables: dict[dict[str, list[Any]]],
                                    courses: list[Course]) \
                                    -> dict[dict[str, list[Any]]]:
        
        interval_variables = {
            course.course_name: {
                section.section_letter: self.__classes_intervals
                                        ( \
                                            start_time_variables[course.course_name][section.section_letter], \
                                            is_present_variables[course.course_name][section.section_letter],\
                                            course.course_name,
                                            section.section_letter,
                                            section.lectures
                                        )

                for section in course.sections
            }
            for course in courses
        }


    def __classes_intervals(self, \
                            start_time_variables: list[Any], \
                            is_present_variables: list[Any], \
                            course_name:str, \
                            section_letter:str, \
                            lecture: Lecture)-> list[Any]:
        
        model = cp_model.CpModel()
        intervals = []

        intervals.append(model.new_optional_fixed_size_interval_var(
                          start = start_time_variables[0], \
                          size = lecture.durations[0], \
                          is_present = is_present_variables[0], \
                          name = f"{course_name}_section_{section_letter}_" \
                               + f"lecture_interval" \
                        ))

        for i in range(1, min(len(start_time_variables), len(is_present_variables))):
                     intervals.append(model.new_optional_fixed_size_interval_var(
                          start = start_time_variables[i], \
                          size = lecture.durations[i], \
                          is_present = is_present_variables[i], \
                          name = f"{course_name}_section_{section_letter}_" \
                               + f"other_class_interval", \
                     ))

        return intervals



        
