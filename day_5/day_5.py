import math

#Calculates the number of units remaining after a polymer activates.
def day_5_1(filename):
    input_file = open(filename)
    polymer = list(input_file.read())
    reacted_polymer = react_polymer(polymer)
    input_file.close()
    return len(reacted_polymer)

#Finds polymer after it has reacted.
def react_polymer(polymer):
    i = 0
    while i < len(polymer) and i+1 < len(polymer)-1:
        #Removes matching pairs of units (letters) if one unit is lowercase and one is uppercase
        while (polymer[i].upper() == polymer[i+1].upper() and
               ((polymer[i].isupper() and polymer[i+1].islower()) or
                (polymer[i].islower() and polymer[i+1].isupper()))):
            if i >= len(polymer) or i+1 >= len(polymer):
                return polymer
            if i < 0:
                i += 1
                continue

            polymer.pop(i)
            polymer.pop(i)
            i -= 1
        i += 1
    return polymer

#Finds the smallest polymer in units (letters) after removing a unit from the polymer.
def day_5_2(filename):
    input_file = open(filename)
    polymer_string = input_file.read()
    polymer = list(polymer_string)
    unique_units = get_unique_units(polymer_string)
    min_polymer_no = math.inf
    for unit in unique_units:
        removed_unit_polymer = [i for i in polymer if i != unit]
        removed_unit_polymer = [j for j in removed_unit_polymer if j != unit.lower()]
        react_polymer_size = len(react_polymer(removed_unit_polymer))
        if react_polymer_size < min_polymer_no:
            min_polymer_no = react_polymer_size
    input_file.close()
    return min_polymer_no

#Gets unique units (letters) as upper case from a polymer
def get_unique_units(polymer_string):
    unique_units = set(list(polymer_string.upper()))
    return unique_units

print("The number of units remaining is", day_5_1("day_5_input.txt"))
print("The shortest polymer that can be produced is", day_5_2("day_5_input.txt"), "units long.")
