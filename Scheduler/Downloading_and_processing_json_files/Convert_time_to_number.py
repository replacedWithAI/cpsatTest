 # time reletive to the num minutes in a day
def start_time_in_minutes(weekday: str, start_time: str) -> int:
    if (len(start_time) == 5):
        hour = int(start_time[:2])
        minutes = int(start_time[3:])
    elif (len(start_time) == 4):
        hour = int(start_time[:1])
        minutes = int(start_time[2:])
    else: 
        print("Start time is wrong: " + start_time)
        hour = 0
        minutes = 0

    start_time = hour*60 + minutes # max: 1440
    weekday_number = convert_day_into_number(weekday)
    return [weekday_number, start_time]


# time relative in minutes relative to 10 days
def time_in_ten_days_minutes(time: int, day: str, curr_term: str) -> int:
    return (curr_term * 10080) + (day * 1440) + time # max 14400

def convert_day_into_number(day: str) -> int:
    if day == "M":
        return int(0)
    elif day == "T":
        return int(1)
    elif day == "W":
        return int(2)
    elif day == "R":
        return int(3)
    elif day == "F": 
        return int(4)
    else:
        print("Day isn't any of these: " + day)
        exit()

def terms_in_this_section(term: str) -> list[int]:
    if term == 'F' or 'S1':
        return [0]
    elif term == 'W' or 'S2':
        return [1]
    elif term == 'Y' or 'SU':
        return [0, 1]