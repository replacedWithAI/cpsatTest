from dataclasses import dataclass
from LabsOrTutorials import LabsOrTutorials

@dataclass
class Lectures:
    activity_name: str
    days: list[str]
    start_times: list[str]
    durations: list[int]
    lab_or_tutorials: list[LabsOrTutorials]