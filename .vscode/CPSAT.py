import json
from pathlib import Path

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
    department_jsons = list
    requested_department_names = list[str]

    def __download_department_jsons(user_path: Path, department_names):
        if not user_path.exists():
            print("Path {user_path} does not exist")
            return
        
        if user_path.is_file():
            print("This is a file, not a path. Give the folder that the file's in")
            return
        
        department_jsons = list
        
        for i in department_names:
            try: 
                with user_path.open(department_names[i] + ".json", "r", encoding = "uft-8") as department_json:
                    department_jsons.append(json.load(department_json))
                
            except FileNotFoundError:
                print("Can't find the department file in your path")
                continue
            
        return department_jsons
    
    def get_department_jsons(self):
        print(self.department_jsons)
        return self.department_jsons
    
    def get_department_names(self):
        print(self.department_jsons)
        return self.requested_department_names

    def __init__(self, user_path: Path, requested_department_names):
        self.department_jsons = self.download_department_jsons(user_path, requested_department_names)
        self.department_names = requested_department_names
        
department_json_path = Path(input("Yo give me your department file path"))

requested_departments = list[str]
requested_departments.append(input("Ok nice, now give me the departments and type '-1' to leave"))

while (requested_departments[-1] != "-1"):
    requested_departments.append(input)

department_json_retriever = Department_json_retriever(department_json_path, requested_departments)
department_json_retriever.get_department_jsons()
        
