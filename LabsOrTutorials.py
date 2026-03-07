from dataclasses import dataclass

@dataclass
class LabsOrTutorials:
    activity_name: str
    days: list[str]
    start_times: list[str]
    durations: list[int]