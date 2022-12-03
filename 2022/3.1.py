# https://adventofcode.com/2022/day/3

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
#    Uppercase item types A through Z have priorities 27 through 52.
#    Lowercase item types a through z have priorities 1 through 26.

sum = 0
nr = 0

with open('3_input.txt') as input_file:
    for uncleanLine in input_file:
        nr = nr + 1
        line = uncleanLine.strip()                    # Remove a Newline Character From the String 
        half = int(len(line)/2)             # /2 returns double
        left = line[0 : half]               # Get the characters from position x to position y (not included):
        right = line[half : len(line)]
        print(left, ' ', right)
        for l in left:
            for r in right:
                if l == r:
                    print(l, " ", r)
        # Element finden, das in beiden Hälften vorkommt
        # Prioriät messen, Summe bilden