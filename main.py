import json
from pathlib import Path
from typing import Any
from dataclasses import dataclass
import Json_departments_to_server_writer
from Course_json_string_retriever import Course_json_retriever
from Extract_course_data import Course_file_extractor
from Class_sessions import Class_sessions
from Lecture import Lecture
from Sections import Sections
from Course import Course

json_departments_to_server_writer = Json_departments_to_server_writer
department_json_path = json_departments_to_server_writer.get_files()
del json_departments_to_server_writer
print(department_json_path)

requested_courses = [input("Ok nice, now give your course names and type '-1' to leave")]
while (requested_courses[-1] != "-1"):
    requested_courses.append(input("List another or type '-1' to leave"))
del(requested_courses[-1])
print(requested_courses)

Course_json_retriever = Course_json_retriever(department_json_path, requested_courses)
course_jsons = Course_json_retriever.get_course_jsons()
del Course_json_retriever
        
Course_file_extractor = Course_file_extractor(course_jsons)
course = (Course_file_extractor.get_list_of_courses_data())[0]
print(course.course_code)
