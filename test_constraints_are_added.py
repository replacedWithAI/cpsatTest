import Extract_course_jsons_and_data_types
from Scheduler.CPSAT.CPSAT import Schedule_maker

main_obj = Extract_course_jsons_and_data_types
courses = main_obj.Course_file_extractor.get_list_of_courses_data()
CPSAT_obj = Schedule_maker(["Mon1", [0, 0]], courses)

