from dataclasses import dataclass
# from LabsOrTutorials import LabsOrTutorials
from Scheduler.lib.Data_types.Lecture import Lecture

@dataclass
class Section:
    term: list[int]
    section_letter: str
    professor: str
    lectures: Lecture