from dataclasses import dataclass

@dataclass
class Other_class_session:
    activity_name: list[str]
    start_times: list[list[str, int]]
    global_start_times: list[int]
    duration: list[int]
    global_end_times: list[int]
    # Feel like campus isn't needed here; odds that lab/tutorial campus is 
    #   different than lecture?