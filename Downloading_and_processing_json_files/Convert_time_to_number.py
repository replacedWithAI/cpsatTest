 # time reletive to the num minutes in a day
def start_time_in_minutes(weekday: str, start_time: str) -> int:
    hour = start_time[:2]
    minutes = start_time[3:]
    start_time = hour*60 + minutes # max: 1440
    return [weekday, start_time]


# time relative in minutes relative to 10 days
def time_in_ten_days_minutes(start_time: int, day: str, term: str) -> int:
    return (term * 10080) + (day * 1440) + start_time # max 14400