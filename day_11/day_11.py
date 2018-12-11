#Day 11 Serial Number
SERIAL_NUMBER = 7315

'''Gets the top-left fuel cell of a 3x3 grid
with the largest total power (Sum of all numbers in the grid)'''
def day_11_1(serial_number):
    fuel_cell_list = get_fuel_cell_list(serial_number)
    largest_cell_power = get_largest_cell_power(fuel_cell_list, 3, 1)
    return largest_cell_power['max_coordinates']

#Populates the grid of fuel cells with their power
def get_fuel_cell_list(serial_number):
    fuel_cell_list = []
    for i in range(1, 301):
        fuel_cell_list.append([get_power_level(i, j, serial_number)
                               for j in range(1, 301)])
    return fuel_cell_list

#Gets the 100th digit of a number
def get_hundreth_digit(num):
    if num < 100:
        return 0
    return (num // 100) % 10

#Gets the power level for a fuel cell
def get_power_level(i, j, serial_number):
    rack_id = i+10
    power_level = (rack_id*j+serial_number)*rack_id
    power_level = get_hundreth_digit(power_level)
    power_level -= 5
    return power_level

#Gets the largest fuel cell power and its top left coordinates
def get_largest_cell_power(fuel_cell_list, square_size, part):
    max_cell_power = -40
    max_cell_top_left_coordinates = []
    for i in range(0, 300-(square_size-1)):
        cell_rows = fuel_cell_list[i:i+square_size]
        for j in range(0, 300-(square_size-1)):
            cell_power = 0
            for cell_row in cell_rows:
                cell_power += sum(cell_row[j:j+square_size])
            if cell_power > max_cell_power:
                max_cell_power = cell_power
                if part == 2:
                    max_cell_top_left_coordinates = [i+1, j+1, square_size]
                else:
                    max_cell_top_left_coordinates = [i+1, j+1]


    return {'max_coordinates': max_cell_top_left_coordinates, 'max_power': max_cell_power}

#Gets the max power and the size of the fuel cells
#TODO: Need to optimize this more. Takes 15 minutes to get an answer.
def day_11_2(serial_number):
    fuel_cell_list = get_fuel_cell_list(serial_number)
    max_coordinates = get_max_coordinates_with_varying_sizes(fuel_cell_list)
    return max_coordinates

'''Gets the maximum coordinates with squares that range from
   the minimum to the maximum size of the grid.'''
def get_max_coordinates_with_varying_sizes(fuel_cell_list):
    max_cell_power = -360000
    largest_cell_power = {}
    for i in range(1, 301):
        cell_power = get_largest_cell_power(fuel_cell_list, i, 2)
        if cell_power['max_power'] > max_cell_power:
            max_cell_power = cell_power['max_power']
            largest_cell_power = cell_power
    return largest_cell_power['max_coordinates']

print('The top left coordinate of the 3 x 3 square that has the maximum power is',
      day_11_1(SERIAL_NUMBER))

print('The size and top-left coordinate of the square that has the maximum power is',
      day_11_2(SERIAL_NUMBER))
