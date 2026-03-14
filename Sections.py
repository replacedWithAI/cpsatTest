from dataclasses import dataclass
# from LabsOrTutorials import LabsOrTutorials
from Lecture import Lecture

@dataclass
class Section:
    term: str
    section_letter: str
    professor: str
    lectures: Lecture