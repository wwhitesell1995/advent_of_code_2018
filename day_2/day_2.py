from collections import Counter

#Calculates a checksum of the number of lines that have 2 or 3 occurances of the same letter.
def day_2_1(filename):
    file = open(filename)
    checksum_counts = {"two_letter_count": 0, "three_letter_count": 0}
    for line in file:
        letter_counts=Counter(line)
        checksum_counts["two_letter_count"] += int(2 in letter_counts.values())
        checksum_counts["three_letter_count"] += int(3 in letter_counts.values())
    
    file.close()        
    return checksum_counts["two_letter_count"] * checksum_counts["three_letter_count"]
        
#Finds the common letters between two IDs that have a one letter difference between them.
def day_2_2(filename):
    lines = file_to_list(filename)
    
    for line1 in lines:
        for line2 in lines:
            if len(line1)==(len(get_letter_list(line1,line2))+1):
                list_of_letters=get_letter_list(line1,line2)
                return ''.join(list_of_letters)
        
    
    return "No correct box IDs found!"

#Converts lines in a file to a list.
def file_to_list(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return lines
    
#Returns a list of letters that are in both lines.
def get_letter_list(line1, line2):
    list_of_letters=[]
    for i in range(0, len(line1)):
        if line1[i]==line2[i]:
            list_of_letters.append(line1[i])
    
    return list_of_letters
    
print("The checksum for the list of Box IDs is", day_2_1("day_2_input.txt"))
print("The letters for the prototype boxes are", day_2_2("day_2_input.txt"))