from dataclasses import dataclass
from Other_class_sessions import Other_class_session

@dataclass
class Lecture:
    activity_name: str
    days: list[str]
    start_times: list[str]
    durations: list[int]
    durations.setdefault([0])
    campus: list[str]
    other_class_sessions: list[Other_class_session]