def is_date_title(line):
    if "-" in line and "周" in line:
        if line[line.index("周") - 2].isnumeric() or line.count("-") == 3:
            return True

    return False


# a day text should contain date title on the first line
def is_day(line):
    # if line is not empty
    if line:
        title = line.splitlines()[0]
        return is_date_title(title)
    else:
        return False


# calculate time summary and print
# average is a flag to determine if average if printed or not
def print_time_usage(days, average):
    lab = 0
    play = 0
    code_work = 0
    time_work = 0
    efficiency_work = 0
    meditation = 0
    study = 0
    misc = 0
    read = 0
    think = 0
    tracer = 0

    for day in days:
        # print(day.date)
        lab += day.lab_work_time
        play += day.play_time
        code_work += day.code_work_time
        time_work += day.time_work_time
        efficiency_work += day.efficiency_work_time
        meditation += day.meditation_time
        study += day.study_time
        misc += day.misc_time
        read += day.read_time
        think += day.contemplate_time
        tracer += day.tracer

    # calculate daily average if specified:
    if average:
        lab = lab / len(days)
        play = play / len(days)
        code_work = code_work / len(days)
        time_work = time_work / len(days)
        efficiency_work = efficiency_work / len(days)
        meditation = meditation / len(days)
        study = study / len(days)
        misc = misc / len(days)
        read = read / len(days)
        think = think / len(days)
        tracer = tracer / len(days)

        print("Average Lab work: ", int(lab / 60), " hours", lab % 60, "mins")
        print("Average Play: ", int(play / 60), " hours", play % 60, "mins")
        print("Average Code work: ", int(code_work / 60), " hours", code_work % 60, "mins")
        print("Average Time work: ", int(time_work / 60), " hours", time_work % 60, "mins")
        print("Average Efficiency work: ", int(efficiency_work / 60), " hours", efficiency_work % 60, "mins")
        print("Average Meditation: ", int(meditation / 60), " hours", meditation % 60, "mins")
        print("Average Study: ", int(study / 60), " hours", study % 60, "mins")
        print("Average Misc: ", int(misc / 60), " hours", misc % 60, "mins")
        print("Average Read: ", int(read / 60), " hours", read % 60, "mins")
        print("Average Think: ", int(think / 60), " hours", think % 60, "mins")
        print("tracer: ", int(tracer / 60), " hours", tracer % 60, "mins")
        print("Total day count:", len(days))

    else:
        print("Lab work: ", int(lab / 60), " hours", lab % 60, "mins")
        print("Play: ", int(play / 60), " hours", play % 60, "mins")
        print("Code work: ", int(code_work / 60), " hours", code_work % 60, "mins")
        print("Time work: ", int(time_work / 60), " hours", time_work % 60, "mins")
        print("Efficiency work: ", int(efficiency_work / 60), " hours", efficiency_work % 60, "mins")
        print("Meditation: ", int(meditation / 60), " hours", meditation % 60, "mins")
        print("Study: ", int(study / 60), " hours", study % 60, "mins")
        print("Misc: ", int(misc / 60), " hours", misc % 60, "mins")
        print("Read: ", int(read / 60), " hours", read % 60, "mins")
        print("Think: ", int(think / 60), " hours", think % 60, "mins")
        print("tracer: ", int(tracer / 60), " hours", tracer % 60, "mins")
        print("Total day count:", len(days))


# calculate focus time and print.
# focus time includes time spent in activities which requires a state of
# mindfulness awareness
def print_focus_time(days):
    daily_focus_time = 0
    focus_time = 0
    meditation_time = 0
    play_time = 0
    target_time = 0
    work_day = 0
    play_day = 0
    sleep_time = 0
    avg_sleep_time = 0

    for day in days:
        daily_focus_time = day.code_work_time + day.study_time + day.time_work_time \
                    + day.efficiency_work_time + day.misc_time + day.ta_time \
                    + day.lab_work_time + day.read_time + day.contemplate_time \
                    + day.dream_time

        focus_time += daily_focus_time
        sleep_time += day.sleep_time

        if daily_focus_time > 600:
            # print("Focus day:", day.date, ":", int(daily_focus_time / 60), "hours", daily_focus_time % 60, "mins")
            work_day += 1
        elif day.play_time > 600:
            # print("Play day:", day.date, ":", int(day.play_time / 60), "hours", day.play_time % 60, "mins")
            play_day += 1

        meditation_time += day.meditation_time

        play_time += day.play_time
        target_time += day.tracer

    # print out accumulative focus, play, sleep and meditation time
    avg_sleep_time = round(sleep_time / len(days))
    print("Average sleep time: ", int(avg_sleep_time / 60), "hours", avg_sleep_time % 60, "mins")
    print("Total sleep time: ", int(sleep_time / 60), "hours", sleep_time % 60, "mins")
    print("Total focus time: ", int(focus_time / 60), "hours", focus_time % 60, "mins")
    print("Total meditation time: ", int(meditation_time / 60), "hours",
          meditation_time % 60, "mins")
    print("Total play time: ", int(play_time / 60), "hours", play_time % 60, "mins")
    print("Target time trace: ", int(target_time / 60), "hours", target_time % 60, "mins")
    print("\tWork day:", work_day)
    print("\tPlay_day:", play_day)



