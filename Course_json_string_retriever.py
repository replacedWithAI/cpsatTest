from typing import Any
from pathlib import Path

def __get_department_codes(requested_course_names: list[str]) -> list[str]: # needs to methodology later
    department_codes = list[str]
    for course_name in requested_course_names:
        department_codes.append(course_name[0:5])
    return department_codes

def __get_course_codes(requested_course_names: list[str]) -> list[str]:
    course_codes = list[str]
    for course_code in requested_course_names:
        course_codes.append(course_code[6:9])
    return course_codes

def __open_department_jsons(user_path: Path, department_codes: list[str]) -> list[dict[str, Any]]:
    department_data = list
    for department in department_codes:
        try: 
            with user_path.open(department + ".json", "r", encoding = "uft-8") as department_json:
                current_department_data = department_json.read_text()
                department_data.append(current_department_data)
        except FileNotFoundError:
            print("Can't find the department file in your path")
            continue
    return department_data
    
def __download_course_json_strings(department_data: list[dict[str, Any]], 
        department_codes: list[str], course_codes: list[str]) -> list[dict[str, Any]]:
    course_json_strings = list[dict[str, Any]]
    index = 0
    courses = department_data.get("courses", [])
    for course in courses:
        key = course.get("key", [])
        code = key.get(code, str)
        department = key.get(department, str)
        if code == course_codes[index] and department == department_codes[index]:
            course_json_strings.append(course)
        index += 1
    return course_json_strings

def get_department_jsons(self):
    print(self.department_jsons)
    return self.department_jsons

def __init__(self, user_path: Path, requested_course_names):
    department_codes = self.__get_department_codes(requested_course_names)
    course_codes = self.__get_course_codes(requested_course_names)
    department_data = self.__open_department_jsons(user_path, department_codes)
    self.course_json_strings = self.__download_course_json_strings(department_data, department_codes, course_codes)