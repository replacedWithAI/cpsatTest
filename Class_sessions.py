from dataclasses import dataclass

@dataclass
class Class_sessions:
    activity_name: list[str]
    days: list[str]
    start_times: list[str]
    end_times: list[str]
    # Feel like campus isn't needed here; odds that lab/tutorial campus is different than lecture?