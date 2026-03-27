from ortools.sat.python import cp_model
from lib.Data_types.Course import Course
from lib.Data_types.Sections import Section

class Contraint_adder:
    def __init__(self,\
                 interval_variables: dict[dict[str, list[any]]], \
                 courses: list[Course], \
                 model: cp_model):
        
        self.__add_no_overlap_constraint(interval_variables, courses, model)
    

    def __link_local_global_start()
        
    def __add_no_overlap_constraint(self, 
                                    interval_variables: dict[dict[str, list[any]]], \
                                    courses: list[Course], \
                                    model: cp_model):
        
        for course in courses:
            for section in course.sections:

                for i in range(len(interval_variables[course.course_name]
                                                     [section.section_letter])):
                    model.add_no_overlap(interval_variables[course.course_name]
                                                           [section.section_letter]
                                                           [i])
        return
    
    