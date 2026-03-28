from typing import Any
from ortools.sat.python import cp_model
from lib.Data_types.Course import Course
from Scheduler.CPSAT.Make_CPSAT_variables import CPSAT_variable_maker
from Scheduler.CPSAT.Add_CPSAT_constraints import Constraint_adder

class Scheduler:
    def __add_courses_to_CPSAT(courses: list[Course], model: cp_model):
        CPSAT_variables = CPSAT_variable_maker(courses, model)
        start_time_variables = CPSAT_variables.start_time_variables
        is_present_variables = CPSAT_variables.is_present_variables
        interval_variables = CPSAT_variables.interval_variables
        return
    
    def __add_constraints(is_present_variables: dict[dict[dict[int, Any]]], \
                          interval_variables: dict[dict[dict[int, Any]]], \
                          courses: list[Course], \
                          model: cp_model):
        Constraint_adder(is_present_variables, interval_variables, courses, model)
        return
        
    def __solve_for_optimum():
        return

    def __init__(self, courses: list[Course]):
        model = cp_model.CpModel()
        self.__add_courses_to_CPSAT(courses, model)
        self.__add_constraints

        #add_courses_to_CPSAT(model)
        #add_constraints(model)
        #solve_for_optimum(model)

