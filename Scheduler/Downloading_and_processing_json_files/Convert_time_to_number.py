 # time reletive to the num minutes in a day
def start_time_in_minutes(start_time: str, weekday: str, curr_term: int) -> list[int]:
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
    return [start_time, weekday_number, curr_term]


# time relative in minutes relative to 10 days
def time_in_ten_days_minutes(time: int, day: str, curr_term: str) -> int:
    return (curr_term * 7200) + (day * 1440) + time # max 14400

def convert_day_into_number(day: str) -> int:
    if day == "M":
        return 0
    elif day == "T":
        return 1
    elif day == "W":
        return 2
    elif day == "R":
        return 3
    elif day == "F": 
        return 4
    else:
        print("Day isn't any of these: " + day)
        exit()

def terms_in_this_section(term: str) -> list[int]:
    # print(term)
    if term == 'F' or term == 'S1':
        return [0]
    elif term == 'W' or term == 'S2':
        return [1]
    elif term == 'Y' or term == 'SU':
        return [0, 1]