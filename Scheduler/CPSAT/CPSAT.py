from typing import Any
from ortools.sat.python import cp_model
from lib.Data_types.Course import Course
from Scheduler.CPSAT.Make_CPSAT_variables import CPSAT_variable_maker
from Scheduler.CPSAT.Add_CPSAT_constraints import Constraint_adder

class Scheduler:
    def __add_courses_to_CPSAT(self, courses: list[Course], model: cp_model):
        CPSAT_variables = CPSAT_variable_maker(courses, model)
        self.start_time_variables = CPSAT_variables.start_time_variables
        self.is_present_variables = CPSAT_variables.is_present_variables
        self.interval_variables = CPSAT_variables.interval_variables

        self.intervals_by_day = CPSAT_variables.intervals_by_day
        self.days_present = CPSAT_variables.days_present
        return
    
    def __add_constraints(self,
                          unavailable_hours: list[str, list[int, int]],
                          intervals_by_day: dict[str, list[Any]],
                          days_present: list[Any],
                          interval_variables: dict[dict[dict[int, Any]]],
                          courses: list[Course],
                          model: cp_model):
        Constraint_adder(unavailable_hours, intervals_by_day, days_present, 
                         interval_variables, courses, model)
        return
        
    def __solve_for_objectives():
        return

    def __init__(self, courses: list[Course]):
        model = cp_model.CpModel()
        self.__add_courses_to_CPSAT(courses, model)
        self.__add_constraints
        self.__solve_for_objectives

        #add_courses_to_CPSAT(model)
        #add_constraints(model)
        #solve_for_optimum(model)

