from typing import Any
from Scheduler.lib.Data_types.Course import Course
from Scheduler.lib.Data_types.Sections import Section
from Scheduler.lib.Data_types.Lecture import Lecture
from Scheduler.lib.Data_types.Other_class_sessions import Other_class_session
from Scheduler.Downloading_and_processing_json_files.Convert_time_to_number import start_time_in_minutes
from Scheduler.Downloading_and_processing_json_files.Convert_time_to_number import time_in_ten_days_minutes
from Scheduler.Downloading_and_processing_json_files.Convert_time_to_number import terms_in_this_section


class Course_file_extractor:
    def __make_course_obj(self, course_jsons: list[dict[str, Any]]) -> list[Course]:
        courses = []
        
        for course_json in self.course_jsons:
            course_key = course_json.get("key")
            section_json = course_json.get("schedule")
            course_obj = Course( course_key.get("faculty"), course_key.get \
                                ("dept"), course_key.get("code"), \
                                course_key.get("credit"),
                                course_json.get("name"), course_json.get("prereq"), \
                                self.__make_section_obj(section_json) ) 
            courses.append(course_obj)

        return courses
    

    def __make_section_obj(self, section_jsons: list[dict[str, Any]]) -> list[Section]:
        Sections = []

        for section_json in section_jsons:
            class_session_jsons = section_json.get("classes")
            term = terms_in_this_section( section_json.get("term") )
            section_obj = Section( term, \
                                   section_json.get("section"), \
                                   self.__get_section_professor(class_session_jsons), \
                                   self.__make_lecture_obj(class_session_jsons, \
                                                           term) )
            Sections.append(section_obj)

        return Sections
    

    def __get_section_professor(self, class_session_jsons: list[dict[str, Any]]) -> str:
        lecture_json = class_session_jsons[0] #RHS will be list[dict[str, Any]]
        if (lecture_json.get("professor") is None):
            return ""
        return lecture_json.get("professor")
    
    
    def __make_lecture_obj(self, class_session_jsons: list[dict[str, Any]], \
                           term: list[int]) -> list[Lecture]:
        lecture_json = class_session_jsons[0] #RHS will be list[dict[str, Any]]
        start_times = []
        global_start_times = []
        durations = []
        global_end_times = []
        campus = []
        lecture_timeslots = lecture_json.get("timeslot")
        
        for curr_term in term:
            for lecture_timeslot in lecture_timeslots:
                start_times.append( start_time_in_minutes(lecture_timeslot.get("weekday"), 
                                                          lecture_timeslot.get("time") ))
                
                global_start_times.append(time_in_ten_days_minutes(
                                                        start_times[-1][1],
                                                        start_times[-1][0],
                                                        curr_term))

                durations.append(int( lecture_timeslot.get("duration") ))

                global_end_times.append( global_start_times[-1] + durations[-1] )

                campus.append( lecture_timeslot.get("campus") )
        
        return Lecture( lecture_json.get("name"), start_times, global_start_times, \
                        durations, global_end_times, campus, \
                        self.__make_class_sessions_list(class_session_jsons, curr_term) )
    

    def __make_class_sessions_list(self, class_session_jsons: list[dict[str, Any]], curr_term: int) \
                             -> list[Other_class_session]: #feel like name should be less abstract
        list_class_sessions = []
        class_session_jsons = class_session_jsons[1:]

        # each class session has its list of timeslots
        for class_session_json in class_session_jsons:

            class_session_timeslot_jsons = class_session_json.get("timeslot")
            list_class_sessions.append( self.__make_class_sessions(
                                                class_session_timeslot_jsons, curr_term) )
        
        return list_class_sessions
    
        
    def __make_class_sessions(self, class_session_timeslot_jsons: list[dict[str, Any]],
                                      curr_term: int) -> Other_class_session:
        session_names = []
        start_times = []
        global_start_times = []
        durations = []
        global_end_times = []

        for class_session_timeslot_json in class_session_timeslot_jsons:

            session_names.append( class_session_timeslot_json.get("name"))
            
            start_times.append( start_time_in_minutes(class_session_timeslot_json.get("weekday"), \
                                                      class_session_timeslot_json.get("time") ))
            
            global_start_times.append( time_in_ten_days_minutes(start_times[-1][1],
                                        start_times[-1][0],
                                        curr_term) )
            
            durations.append(int( class_session_timeslot_json.get("duration") ))

            global_end_times.append( global_start_times[-1] + durations[-1] )
        
        return Other_class_session(session_names, start_times, global_start_times,
                                   global_end_times, durations)
    
    
    def get_list_of_courses_data(self) -> Course:
        return self.courses
    
    
    def __init__(self, course_jsons: list[dict[str, Any]]):
        self.course_jsons = course_jsons
        self.courses = self.__make_course_obj(course_jsons)
        del course_jsons