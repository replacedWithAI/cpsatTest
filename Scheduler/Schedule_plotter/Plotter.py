import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from typing import Any

class Plotter:
    def __init__(self, all_chosen_courses: list[Any]):
        self.__make_plot(all_chosen_courses)


    def __make_plot(self, all_chosen_courses: list[Any]):
        fig, schedule = plt.subplots()

        schedule.set_ylim(0, 1440)
        schedule.set_xlim(0, 9)

        schedule.set_xlabel("Weekdays")
        schedule.set_ylabel("Time")

        schedule.xaxis.set_major_locator(MultipleLocator(1)) # setting ticks
        schedule.set_xticklabels(["Mon1", "Tue1", "Wed1", "Thu1", "Fri1",
                                  "Mon2", "Tue2", "Wed2", "Thu2", "Fri2"])
        
        schedule.yaxis.set_major_locator(MultipleLocator(60))
        plt.gca().invert_yaxis()
        schedule.set_yticklabels(["1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM",
                                  "5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM",
                                  "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", 
                                  "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", 
                                  "7:00 PM", "8:00 PM", "9:00 PM","10:00 PM", "11:00 PM", 
                                  "12:00 AM"])
        
        colours = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 
                   'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']
        colour_index = 0

        for course in all_chosen_courses:
            colour = colours[colour_index]
            colour_index += 1

            for curr_class in course:
                name = str(curr_class.name)
                day = curr_class.start_expr() // 1440
                hour = curr_class.start_expr() % 1440
                duration = curr_class.end_expr() - curr_class.start_expr()
                print(hour)

                interval = schedule.bar(day, duration, bottom=hour, label = name,
                                        facecolor=colour)
                
                schedule.bar_label(interval, labels = [name],label_type="center",
                                   wrap = True)
                
                schedule.xaxis_date()
                schedule.figure.autofmt_xdate()

        schedule.grid(True)
        plt.show()


    