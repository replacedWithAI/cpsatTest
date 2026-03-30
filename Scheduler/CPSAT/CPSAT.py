from typing import Any
from ortools.sat.python import cp_model
from Scheduler.lib.Data_types.Course import Course
from Scheduler.CPSAT.Make_CPSAT_variables import CPSAT_variable_maker
from Scheduler.CPSAT.Add_CPSAT_constraints import Constraint_adder
from Scheduler.CPSAT.Solve_CPSAT_objectives import Solve_best_schedule

class Schedule_maker:
    def __init__(self, 
                 unavailable_hours: list[str, list[int, int]],
                 courses: list[Course], commute_times: int =  0):
        
        model = cp_model.CpModel()

        (self.start_time_variables, self.is_present_variables,
         self.interval_variables, self.intervals_by_day,
         self.days_present) = self.__add_courses_to_CPSAT(courses, model)
        
        self.__add_constraints(unavailable_hours, self.intervals_by_day,
                               self.days_present, self.interval_variables,
                               courses, model)
        
        self.__solve_for_objectives(self.intervals_by_day, self.days_present,
                                    model, commute_times)
    

    def __add_courses_to_CPSAT(self, courses: list[Course], model: cp_model
                               ) -> tuple:
        CPSAT_variables = CPSAT_variable_maker(courses, model)
        start_time_variables = CPSAT_variables.start_time_variables
        is_present_variables = CPSAT_variables.is_present_variables
        interval_variables = CPSAT_variables.interval_variables

        intervals_by_day = CPSAT_variables.intervals_by_day
        days_present = CPSAT_variables.days_present
        return (start_time_variables, is_present_variables, interval_variables, 
               intervals_by_day, days_present)
    

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
        
    def __solve_for_objectives(self,
                               intervals_by_day: dict[str, list[Any]],
                               days_present: list[Any],
                               model: cp_model,
                               commute_times: int = 0):
        solver = cp_model.CpSolver()
        solver.parameters.log_search_progress = True  # Enable logging
        Solve_best_schedule(intervals_by_day, days_present, model, solver, commute_times)
        return


