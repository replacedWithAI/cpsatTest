from dataclasses import dataclass
from Scheduler.lib.Data_types.Other_class_sessions import Other_class_session

@dataclass
class Lecture:
    activity_name: str
    start_times: list[list[str, int]]
    global_start_times: list[int]
    durations: list[int]
    global_end_times: list[int]
    campus: list[str]
    other_class_sessions: list[Other_class_session]