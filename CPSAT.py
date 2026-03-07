import json
from pathlib import Path
from typing import Any
from dataclasses import dataclass
import Json_departments_to_server_writer
import Course_json_string_retriever
from LabsOrTutorials import LabsOrTutorials
from Lectures import Lectures
from Sections import Sections
from Course import Course

json_departments_to_server_writer = Json_departments_to_server_writer
department_json_path = json_departments_to_server_writer.get_files()

requested_courses = list[str]
requested_courses.append(input("Ok nice, now give your course names and type '-1' to leave"))

while (requested_courses[-1] != "-1"):
    requested_courses.append(input)

Course_json_string_retriever = Course_json_string_retriever(department_json_path, requested_courses)
department_json_retriever.get_department_jsons()
        
