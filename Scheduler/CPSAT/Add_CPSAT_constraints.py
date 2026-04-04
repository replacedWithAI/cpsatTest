from Scheduler.lib.Data_types.Course import Course
from Scheduler.lib.Data_types.Class_sessions import Class_session
from typing import Any
from ortools.sat.python import cp_model

class Constraint_adder:
    def __init__(self,
                 unavailable_hours: list[str, list[int, int]],
                 intervals_by_day: dict[str, list[Any]],
                 days_present: list[Any],
                 interval_variables: dict[dict[dict[int, Any]]], 
                 courses: list[Course], 
                 model: cp_model):
        
        self.__add_no_overlap_constraint(interval_variables, courses, model)
        self.__add_section_per_course_constraint(interval_variables, courses, model)
        self.__add_unavailable_hours_constraint(unavailable_hours, intervals_by_day, model)
        self.__track_used_days(days_present, intervals_by_day, model)

    def __add_section_per_course_constraint(self, 
                                            interval_variables: dict[str, dict[str, dict
                                                                    [str, dict[int, Any]]]], 
                                            courses: list[Course], 
                                            model: cp_model):
        for course in courses:
            course_name = course.course_name
            sections_available = []

            for section in course.sections:

                section_letter = section.section_letter
                classes = section.classes

                lecture_intervals = interval_variables[course_name] \
                                                      [section_letter] \
                                                      [classes[0].activity_name]
                lecture_is_present = lecture_intervals[0].presence_literals()[0]
                curr_section_presence = lecture_is_present
                sections_available.append(curr_section_presence)
                
                self.__add_one_lab_tutorial_per_section(interval_variables,
                                                        curr_section_presence, 
                                                        course_name, 
                                                        section_letter, 
                                                        classes, 
                                                        model)
                                                        
            #print(sections_available)
            model.add(sum(sections_available) == 1)
        return
                
        
    def __add_one_lab_tutorial_per_section(self,
                                           interval_variables: dict[str, dict[str, dict
                                                                   [str, dict[int, Any]]]], 
                                           curr_section_presence: Any, 
                                           course_name: str, 
                                           section_letter: str, 
                                           classes: list[Class_session], 
                                           model: cp_model):
        chooseable_classes = [[]]
        unique_chooseable_class_idx = 0 # suppose can choose from 5 labs, 3 tutorials

        for i in range(len(classes)):
            for j in range(len(classes[i].start_times)):

                curr_is_present_variable = interval_variables[course_name] \
                                                             [section_letter] \
                                                             [classes[i].activity_name] \
                                                             [j] \
                                                             .presence_literals()[0]
                
                is_chooseable_class = (curr_section_presence != curr_is_present_variable)
                if (is_chooseable_class):
                    chooseable_classes[unique_chooseable_class_idx].append(
                                                        curr_is_present_variable)
                    
                    next_chooseable_class_is_unique = (i+1 != len(classes) and \
                                                      "01" in classes[i+1].activity_name)
                    if (next_chooseable_class_is_unique):
                        num_unique_chooseable_classes += 1
                        chooseable_classes.append([])

        print(chooseable_classes)
        for unique_chooseable_class in chooseable_classes:
            if unique_chooseable_class != []:
                model.add(sum(unique_chooseable_class) == curr_section_presence)
        return
    

    def __add_no_overlap_constraint(self, 
                                    interval_variables: dict[str, dict[str, dict
                                                            [str, dict[int, Any]]]], 
                                    courses: list[Course], 
                                    model: cp_model):
        list_of_intervals = [] # yes. your ram is crying. I know
        
        for course in courses: # bro wth is this? yeah I know. We iterate through everything
            for section in course.sections:
                for curr_class in section.classes:
                    for i in range(len(curr_class.start_times)):
                        curr_interval = interval_variables[course.course_name] \
                                                          [section.section_letter] \
                                                          [curr_class.activity_name] \
                                                          [i]
                        list_of_intervals.append(curr_interval)
                        
        model.add_no_overlap(list_of_intervals)
        return # lets never do that again
    

    def __add_unavailable_hours_constraint(self,
                                           unavailable_hours: list[str, list[int, int]],
                                           intervals_by_days: dict[Any],
                                           model: cp_model
                                           ):


        for interval in intervals_by_days[unavailable_hours[0]]: # will need clean up
            unavailable_start = unavailable_hours[1][0]
            unavailable_end = unavailable_hours[1][1]

            interval_in_unavailable_time = (interval.start_expr() >= unavailable_start) \
                                            and (interval.start_expr() + interval.size_expr() \
                                            <= unavailable_end)
            if (interval_in_unavailable_time):
                model.add_bool_and(interval.presence_literals[0]) # set bool = 0
        return


    def __track_used_days(self, 
                          days_present: list[Any], 
                          intervals_by_days: dict[str, list[Any]],
                          model: cp_model):
        curr_day = -1

        for intervals in intervals_by_days.values():
            curr_day += 1
            if intervals == []:
                continue

            curr_day_intervals = []

            for interval in intervals:
                interval_is_present = interval.presence_literals()[0]
                curr_day_intervals.append(interval_is_present)
            model.add_max_equality(days_present[curr_day], curr_day_intervals)

        return
        
                