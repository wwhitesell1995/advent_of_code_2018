#Finds the total frequency of a file (Day 1 Part 1)
def find_total_frequency(filename, frequency=0):
    file = open(filename)
    for line in file:
        frequency += int(line)
    return frequency

#Finds the first duplicate frequency occurance in a file (Day 1 Part 2).
def find_duplicate_frequency(filename, frequency=0):
    file = open(filename)
    frequency_set=set({})
    while(True):
        for line in file:
            if frequency in frequency_set:
                return frequency
            frequency_set.add(frequency)    
            frequency += int(line)
        file.seek(0)
        
print("The frequency of the file is", find_total_frequency("day_1_input.txt"))
print("The first duplicate frequency is", find_duplicate_frequency("day_1_input.txt"))