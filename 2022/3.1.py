# https://adventofcode.com/2022/day/3

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
#    Uppercase item types A through Z have priorities 27 through 52.
#    Lowercase item types a through z have priorities 1 through 26.

sum = 0

with open('3_input.txt') as input_file:
    for newline in input_file:
        line = newline.strip()        # Remove a Newline Character From the String 
        print(line)
        # Zeilen in zwei Hälften aufteilen
        # Element finden, das in beiden Hälften vorkommt
        # Prioriät messen, Summe bilden