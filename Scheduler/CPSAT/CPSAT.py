from ortools.sat.python import cp_model
from typing import Any
from Downloading_and_processing_json_files.Extract_process_course_data import Course_file_extractor
from lib.Data_types.Course import Course

class Scheduler:
    def __define_interval_variables(courses: list[Course]):
        model = cp_model.CpModel
        for course in courses:
            for section in course.sections:
                lecture = section.lectures


    def __add_constraints():
        
    def __solve_for_optimum():

    def __init__(self, course_jsons: list[dict[str, Any]]):
        solver = cp_model.CpModel()

        #add_courses_to_CPSAT()
        #add_constraints()
        #solve_for_optimum()

