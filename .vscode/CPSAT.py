import json

class LabsOrTutorials:
    activity_name: str
    days: list[str]
    start_times: list[str]
    durations: list[int]

class Lectures:
    activity_name: str
    days: list[str]
    start_times: list[str]
    durations: list[int]
    lab_or_tutorials: list[LabsOrTutorials]

class Sections:
    terms: str
    section_letter: str
    professor: str
    lectures: list[Lectures]

class Course:
    faculty: str
    department: str
    course_code: str
    credits: str
    course_name: str
    campus: str
    prerequisites: list[str]
    sections: list[Sections]

class Department_json_retriever:
    departmentJsons = auto
    departmentNames = list[str]

    _download_department_jsons(
