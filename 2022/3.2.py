# https://adventofcode.com/2022/day/3#part2

# Find the item type that corresponds to the badges of each three-Elf group. 
# What is the sum of the priorities of those item types?




def findCharInLines(lines):
    for x in lines[0]:
        for y in lines[1]:
            if x == y:
                for z in lines[2]:
                    if y == z:
                        return z



def findPriority(char):
    # ord('a') = 97
    # ord('A') = 65
    #    Lowercase item types a through z have priorities 1 through 26.
    #    Uppercase item types A through Z have priorities 27 through 52.
    priority = 0
    for candidate in range(97, (97+26+1)):           # 26 chars, stop is exclusive --> +1 
        priority = priority + 1
        if candidate == ord(char):
            return priority
    
    for candidate in range(65, (65+26+1)):
        if candidate == ord(char):
            return priority
        priority = priority + 1

sum = 0
sizeOfGroup = 3

with open('3_input.txt') as input_file:
    lines = []
    for uncleanLine in input_file:
        line = uncleanLine.strip()                    # Remove a Newline Character From the String 
        lines.append(line)
        
        if len(lines) == sizeOfGroup:
            char = findCharInLines(lines)
            priority = findPriority(char)
            #print(char, priority)
            sum = sum + priority
            lines.clear()

print(sum)