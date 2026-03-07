from dataclasses import dataclass
# from LabsOrTutorials import LabsOrTutorials
# from Lectures import Lectures
from Sections import Sections

@dataclass
class Course:
    faculty: str
    department: str
    course_code: str
    credits: str
    course_name: str
    campus: str
    prerequisites: list[str]
    sections: list[Sections]