from dataclasses import dataclass

@dataclass
class Class_session:
    activity_name: list[str]
    start_times: list[list[str, int]]
    global_start_times: list[int]
    duration: list[int]
    global_end_times: list[int]
    campus: list[str]