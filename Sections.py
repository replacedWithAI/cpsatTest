from dataclasses import dataclass
# from LabsOrTutorials import LabsOrTutorials
from Lectures import Lectures

@dataclass
class Sections:
    terms: str
    section_letter: str
    professor: str
    lectures: list[Lectures]