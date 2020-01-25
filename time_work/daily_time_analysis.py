import matplotlib.pyplot as plt
from functions import *
import pygal


class Day:
    def __init__(self, text):
        self.text = text.splitlines()
        # self.formatize()
        self.date_title = self.text[0]
        self.date = self.date_title[:self.date_title.index(' ')]  # only x-x format date
        self.month, self.day = self.get_month_day()

        # calculate work time (in min)
        self.lab_work_time = self.calculate_activity_time("lab work:")
        self.play_time = self.calculate_activity_time("浅水欢愉：")
        self.code_work_time = self.calculate_activity_time("code work:")
        self.time_work_time = self.calculate_activity_time("time work:")
        self.efficiency_work_time = self.calculate_activity_time("efficiency work:")
        self.meditation_time = self.calculate_activity_time("坐禅")


    def get_month_day(self):
        dash_index = self.text[0].index("-")
        space_index = self.text[0].index(" ")
        month_str = "".join(self.text[0][0:dash_index])
        day_str = "".join(self.text[0][dash_index + 1:space_index])
        return int(month_str), int(day_str)

    def calculate_activity_time(self, name):
        hours = 0
        mins = 0
        for line in self.text:
            if name in line:
                if "'" in line:
                    hour_index = line.index("'")
                    hour_str = line[hour_index - 1]
                    if hour_str.isnumeric():
                        hours += int(hour_str)
                if '"' in line:
                    min_index = line.index('"')
                    first_non_num_index = min_index - 1

                    while first_non_num_index > 0 and line[first_non_num_index].isnumeric():
                        first_non_num_index -= 1

                    if line[first_non_num_index].isnumeric():
                        min_str = line[first_non_num_index:min_index]
                    else:
                        min_str = line[first_non_num_index + 1:min_index]
                    mins += int(min_str)

        return hours * 60 + mins

    def formatize(self):
        """convert -小时-分 to symbol notation"""
        for i in range(len(self.text)):
            # formatize "小时"
            if "小时" in self.text[i]:
                if self.text[i][self.text[i].index("小时") - 1].isnumeric():  # this is a time expression
                    self.text[i] = self.text[i].replace("小时", "'")
            # formatize "分"
            if "分" in self.text[i]:
                if self.text[i][self.text[i].index("分") - 1].isnumeric():  # this is a time expression
                    self.text[i] = self.text[i].replace("分", '"')


count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
day_text = ""
days = []
inside_day = False

# create list
with open("2019.txt") as time_file:
    for line in time_file:
        if is_date_title(line):
            # last day text ends, add to days list if it is day_text
            if is_day(day_text):
                day = Day(day_text)
                days.append(day)
            # start new day text
            day_text = line

        else:
            day_text += line


# checking if days are counted correct
for day in days:
    count[day.month - 1] += 1

# print result to see
print_time_usage(days)


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

