class Day:
    def __init__(self, text):
        self.text = text.splitlines()
        # self.formatize()
        self.date_title = self.text[0]
        self.date = self.date_title[:self.date_title.index(' ')]  # only x-x format date
        self.month, self.day = self.get_month_day()

        # calculate work time (in min)
        self.sleep_time = self.calculate_activity_time("sleep:")
        self.dream_time = self.calculate_activity_time("dream:")
        self.lab_work_time = self.calculate_activity_time("lab_work:")
        self.play_time = self.calculate_activity_time("浅水欢愉：")
        self.code_work_time = self.calculate_activity_time("code_work:")
        self.time_work_time = self.calculate_activity_time("time_work:")
        self.efficiency_work_time = self.calculate_activity_time("efficiency_work:")
        self.meditation_time = self.calculate_activity_time("坐禅：")
        self.study_time = self.calculate_activity_time("study:")
        self.misc_time = self.calculate_activity_time("misc:")
        self.read_time = self.calculate_activity_time("read:")
        self.contemplate_time = self.calculate_activity_time("think:")
        self.ta_time = self.calculate_activity_time("TA_work:")
        self.tracer = self.calculate_activity_time("浅水欢愉：")

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
            if name in line and ("~" + name) not in line:
                if "'" in line:
                    hour_index = line.index("'")
                    first_non_num_index = hour_index - 1

                    while first_non_num_index >= 0 and line[first_non_num_index].isnumeric():
                        first_non_num_index -= 1

                    if line[first_non_num_index].isnumeric():
                        hour_str = line[first_non_num_index:hour_index]
                    else:
                        hour_str = line[first_non_num_index + 1:hour_index]
                    # add to mins if min_str != ''
                    if hour_str.isnumeric():
                        hours += int(hour_str)

                if '"' in line:
                    min_index = line.index('"')
                    first_non_num_index = min_index - 1

                    while first_non_num_index >= 0 and line[first_non_num_index].isnumeric():
                        first_non_num_index -= 1

                    if line[first_non_num_index].isnumeric():
                        min_str = line[first_non_num_index:min_index]
                    else:
                        min_str = line[first_non_num_index + 1:min_index]

                    # add to mins if min_str != ''
                    if min_str.isnumeric():
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
