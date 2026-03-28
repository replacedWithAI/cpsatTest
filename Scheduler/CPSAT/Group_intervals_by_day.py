from Scheduler.lib.Data_types.Course import Course
from typing import Any

def group_intervals_by_day(self, \
                           courses: list[Course], \
                           interval_variables: dict[dict[dict[int, Any]]]) \
                           -> list[dict[str, list]]:
                
        days = {"Mon1": [], "Tue1": [], "Wed1": [], "Thu1": [], "Fri1": [],
                "Mon2": [], "Tue2": [], "Wed2": [], "Thu2": [], "Fri2": []}
        
        for course in courses:
            for section in course.sections:
                for curr_class in section.classes:
                    for i in range(len(interval_variables[course.course_name]
                                                         [section.section_letter]
                                                         [curr_class.activity_name])):
                        
                        days_key = self.__get_curr_day(curr_class.start_times[i][1])
                        days_key += self.__get_current_term(curr_class.start_times[i][2])
                        days[days_key].append(interval_variables[course.course_name]
                                                                [section.section_letter]
                                                                [curr_class.activity_name]
                                                                [i])
        return days



def __get_current_day(day: int) -> str:
    if (day == 0):
        return "Mon"
    elif (day == 1):
        return "Tue"
    elif (day == 2):
        return "Wed"
    elif (day == 3):
        return "Thu"
    elif (day == 4):
        return "Fri"
    else:
        print("Current day is unreadable: " + str(day))
        return "Mon"


def __get_current_term(term: int) -> str:
     if (term == 0):
        return "1"
     elif (term == 1):
        return "2"
     else:
        print("Current day is unreadable: " + str(term))
        return "1"
              