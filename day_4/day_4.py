from day_4_functions import *

'''Returns the product of the guard id of sleepiest guard 
   with the minute they slept most.'''
def day_4_1(filename):
    input_file = open(filename)
    guard_list = get_sorted_guard_list(input_file)
    guard_minutes = get_guard_minutes(guard_list)
    max_sleep = get_biggest_sleeper_minute_id(guard_minutes)
    input_file.close()
    return max_sleep

#Multiplies the guard id of sleepiest guard with the minute they slept most.
def get_biggest_sleeper_minute_id(guard_minutes):
    max_sleep_guard_id = 0
    guard_sleep_max = 0
    for guard_id in guard_minutes.keys():
        if len(guard_minutes[guard_id]) > guard_sleep_max:
            guard_sleep_max = len(guard_minutes[guard_id])
            max_sleep_guard_id = guard_id
    return max_sleep_guard_id * max(set(guard_minutes[max_sleep_guard_id]),
                                    key=guard_minutes[max_sleep_guard_id].count)

'''Returns the product of the minute that was slept on the most by a guard
   and their guard id.'''
def day_4_2(filename):
    input_file = open(filename)
    guard_list = get_sorted_guard_list(input_file)
    guard_minutes = get_guard_minutes(guard_list)
    max_sleep = get_most_common_sleep_minute(guard_minutes)
    input_file.close()
    return max_sleep

#Multiplies the minute that was slept on the most by a guard and their guard id.
def get_most_common_sleep_minute(guard_minutes):
    max_sleep_minute_guard_id = 0
    max_sleep_minute = 0
    max_no_occurances = 0
    for guard_id in guard_minutes.keys():
        curr_max_sleep_minute = max(set(guard_minutes[guard_id]),
                                    key=guard_minutes[guard_id].count)
        curr_max_no_occurances = guard_minutes[guard_id].count(curr_max_sleep_minute)
        if curr_max_no_occurances > max_no_occurances:
            max_no_occurances = curr_max_no_occurances
            max_sleep_minute = curr_max_sleep_minute
            max_sleep_minute_guard_id = guard_id

    return max_sleep_minute_guard_id * max_sleep_minute

print("The product of the sleepiest guard and the minute they slept most is",
      day_4_1("day_4_input.txt"))

print("The product of the guard and the minute that was most slept on is",
      day_4_2("day_4_input.txt"))
    