# https://adventofcode.com/2022/day/1
# 1.1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

class Elf:
    def __init__(self, number):
        self.number = number
        self.calories = 0

    def add(self, calories):
        self.calories = self.calories + calories



allElfes = []

with open('1_input.txt') as input_file:
    elf = Elf(len(allElfes))
    for line in input_file:
        if line == '\n':
            allElfes.append(elf)
            elf = Elf(len(allElfes)) 
        else:
            elf.add(int(line))
    allElfes.append(elf)


# 1.2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

sortedElfes = sorted(allElfes, key=lambda elf: elf.calories, reverse=True)   
# Sort List of objects by attribute: https://wiki.python.org/moin/HowTo/Sorting#Sortingbykeys

sumTopThree = 0
for i in range(0,3):
    sumTopThree = sumTopThree + sortedElfes[i].calories

print(sumTopThree)
