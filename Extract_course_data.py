from typing import Any
from Course import Course
from Sections import Sections
from Lecture import Lecture
from Class_sessions import Class_sessions

class Course_file_extractor:
    def __make_course_obj(self, course_jsons: list[dict[str, Any]]) -> list[Course]:
        courses = []
        
        for course_json in self.course_jsons:
            course_key = course_json.get("key")
            section_json = course_json.get("schedule")
            course_obj = Course( course_key.get("faculty"), course_key.get("dept"), course_key.get("code"), course_key.get("credit"),
                       course_json.get("name"), course_json.get("prereq"), self.__make_section_obj(section_json) ) 
            courses.append(course_obj)

        return courses

    def __make_section_obj(self, section_jsons: list[dict[str, Any]]) -> list[Sections]:
        sections = []

        for section_json in section_jsons:
            class_session_jsons = section_json.get("classes")
            section_obj = Sections( section_json.get("term"), section_json.get("section"), 
                                   self.__get_section_professor(class_session_jsons), 
                                   self.__make_lecture_obj(class_session_jsons) )
            sections.append(section_obj)

        return sections

    def __get_section_professor(self, class_session_jsons: list[dict[str, Any]]) -> str:
        lecture_json = class_session_jsons[0] #RHS will be list[dict[str, Any]]
        if (lecture_json.get("professor") is None):
            return ""
        return lecture_json.get("professor")
    
    def __make_lecture_obj(self, class_session_jsons: list[dict[str, Any]]) -> list[Lecture]:
        lecture_json = class_session_jsons[0] #RHS will be list[dict[str, Any]]
        lecture_weekdays = []
        lecture_start_times = []
        lecture_end_times = []
        lecture_campus = []
        lecture_timeslots = lecture_json.get("timeslot")
        
        for lecture_timeslot in lecture_timeslots:
            lecture_weekdays.append( lecture_timeslot.get("weekday") )
            lecture_start_times.append( lecture_timeslot.get("time") )
            lecture_end_times.append( self.__calculate_end_times(lecture_start_times[-1], lecture_timeslot.get("duration")) )
            lecture_campus.append( lecture_timeslot.get("campus") )
        
        return Lecture( lecture_json.get("name"), lecture_weekdays, lecture_start_times, lecture_end_times,
                        lecture_campus, self.__make_lab_tutorials(class_session_jsons) )

    def __make_lab_tutorials(self, class_session_jsons: list[dict[str, Any]]) -> list[Class_sessions]: #feel like name should be less abstract
        class_sessions = []
        class_session_jsons = class_session_jsons[1:]

        for class_session_json in class_session_jsons:
            class_session_timeslot_jsons = class_session_json.get("timeslot")
            class_sessions.append( self.__get_class_session_timeslots(class_session_timeslot_jsons) )
        
        return class_sessions
        
    def __get_class_session_timeslots(self, class_session_timeslot_jsons: list[dict[str, Any]]) -> Class_sessions:
        session_names = []
        class_session_weekdays = []
        class_session_start_times = []
        class_session_end_times = []

        for class_session_timeslot_json in class_session_timeslot_jsons:
            session_names.append( class_session_timeslot_json.get("name"))
            class_session_weekdays.append( class_session_timeslot_json.get("weekday") )
            class_session_start_times.append( class_session_timeslot_json.get("time") )
            class_session_end_times.append( self.__calculate_end_times( class_session_start_times[-1], 
                                                                        class_session_timeslot_json.get("duration")) )
        
        return Class_sessions(session_names, class_session_weekdays, class_session_start_times, class_session_end_times)
            
    def __calculate_end_times(self, start_time: str, duration: int) -> str:
        start_time_minutes = int(start_time[3:])
        duration = int(duration)
        if duration + start_time_minutes < 60:
            return start_time[:3] + str(duration + start_time_minutes)
        
        duration -= 60 - start_time_minutes
        start_time_minutes = 0
        duration_hours = 0
        start_time_hours = int(start_time[:1])
        
        while duration > 60:
            duration_hours += 1
            duration -= 60
        return str(start_time_hours + duration_hours) + ":" + str(duration)
    
    def get_list_of_courses_data(self) -> Course:
        return self.courses
    
    def __init__(self, course_jsons: list[dict[str, Any]]):
        self.course_jsons = course_jsons
        self.courses = self.__make_course_obj(course_jsons)
        del course_jsons




    
