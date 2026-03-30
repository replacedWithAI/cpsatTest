import main
from Scheduler.CPSAT.CPSAT import Schedule_maker

main_obj = main
courses = main_obj.Course_file_extractor.get_list_of_courses_data()
CPSAT_obj = Schedule_maker(["Mon1", [0, 0]], courses)

