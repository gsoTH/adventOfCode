# https://adventofcode.com/2022/day/3

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
#    Uppercase item types A through Z have priorities 27 through 52.
#    Lowercase item types a through z have priorities 1 through 26.

sum = 0
nr = 0

def findCharInBothStrings(left, right):
    for l in left:
            for r in right:
                if l == r:
                    return l


def findPriority(char):
    # ord('a') = 97
    # ord('A') = 65
    priority = 0
    for candidate in range(97, (97+26+1)):           # 26 chars, stop is exclusive --> +1 
        priority = priority + 1
        if candidate == ord(char):
            return priority
    
    for candidate in range(65, (65+26+1)):
        if candidate == ord(char):
            return priority
        priority = priority + 1


with open('3_input.txt') as input_file:
    for uncleanLine in input_file:
        nr = nr + 1
        line = uncleanLine.strip()                    # Remove a Newline Character From the String 
        half = int(len(line)/2)                       # /2 returns double
        left = line[0 : half]                         # Get the characters from position x to position y (not included):
        right = line[half : len(line)]
        char = findCharInBothStrings(left, right)
        priority = findPriority(char)
        print(char, priority)
        sum = sum + priority

print(sum)