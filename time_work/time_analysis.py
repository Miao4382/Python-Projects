import matplotlib.pyplot as plt
from functions import *
from day_class import *
import pygal


count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
day_text = ""
line = ""
days = []
inside_day = False

# create list of days
with open("daily_time.txt") as time_file:
    for line in time_file:
        if "浅水欢愉：" in line:
            print(line)
        if is_date_title(line):
            # previous day text ends, add to days list if it is day_text
            if is_day(day_text):
                day = Day(day_text)
                days.append(day)
            # start new day text
            day_text = line

        else:
            day_text += line

    # after reading the last line, convert current day_text to Day and add to days
    day = Day(day_text)
    days.append(day)

# checking if days are counted correct
for day in days:
    count[day.month - 1] += 1

# print result to see
# print_time_usage(days)

# print focus time
# print_focus_time(days)
print_time_usage(days, 0)
print_focus_time(days)

# plot play time and focus time
# focus_time = []
# play_time = []
# day_range = list(range(1, len(days) + 1))
#
# for day in days:
#     daily_focus_time = day.code_work_time + day.study_time + day.time_work_time \
#                        + day.efficiency_work_time + day.misc_time + day.ta_time \
#                        + day.lab_work_time + day.read_time + day.contemplate_time \
#                        + day.meditation_time
#     play_time.append(day.play_time)
#     focus_time.append(daily_focus_time)
#
# plt.scatter(day_range, play_time, c='red')
# plt.scatter(day_range, focus_time, c='blue')
# plt.show()

# For histogram making
# codework_time = []
# labwork_time = []
# timework_time = []
# play_time = []
# meditation_time = []
# xlabels = []
# for day in days:
#     codework_time.append(day.code_work_time)
#     labwork_time.append(day.lab_work_time)
#     timework_time.append(day.time_work_time)
#     play_time.append(day.play_time)
#     meditation_time.append(day.meditation_time)
#     xlabels.append(day.date)
#
# hist = pygal.Bar()
# hist.add('code work', codework_time)
# hist.add('lab work', labwork_time)
# hist.add('time work', timework_time)
# hist.add('play', play_time)
# hist.add('meditation', meditation_time)
# hist.x_labels = xlabels
# hist.render_to_file('time.svg')
# print(xlabels)

