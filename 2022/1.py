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


maxCalories = -1
maxIndex = -1 
for elf in allElfes:
    if elf.calories > maxCalories:
        maxCalories = elf.calories
        maxIndex = elf.number

print(maxCalories)
