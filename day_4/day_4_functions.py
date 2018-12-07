from datetime import datetime

#Sorts the list of actions the guards take by datetime.
def get_sorted_guard_list(input_file):
    guard_list = []
    for line in input_file:
        replace_line = line.replace('[', '')
        guard_list.append(tuple(replace_line.split("] ")))
    sorted_guard_list = sorted(guard_list,
                               key=lambda guardtime:
                               datetime.strptime(guardtime[0], '%Y-%m-%d %H:%M'))
    return sorted_guard_list

#Get the minutes the guards were asleep.
def get_guard_minutes(guard_list):
    guard_minutes = {}
    current_guard = 0
    start_minute = 0
    for time, action in guard_list:
        if "begins shift" in action:
            current_guard = int(action.split('#')[1].split(' ')[0])
        elif "falls asleep" in action:
            start_minute = int(time[time.find(':')+1::])
        elif "wakes up" in action:
            end_minute = int(time[time.find(':')+1::])
            if current_guard in guard_minutes:
                guard_minutes[current_guard].extend(list(range(start_minute, end_minute)))
            else:
                guard_minutes[current_guard] = list(range(start_minute, end_minute))
    return guard_minutes