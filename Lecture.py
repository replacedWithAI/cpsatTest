from dataclasses import dataclass
from Class_sessions import Class_sessions

@dataclass
class Lecture:
    activity_name: str
    days: list[str]
    start_times: list[str]
    end_times: list[str]
    campus: list[str]
    lab_or_tutorials: list[Class_sessions]