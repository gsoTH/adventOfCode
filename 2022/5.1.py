# https://adventofcode.com/2022/day/5

import os
import re

# Pfade zuverlässig angeben: https://stackoverflow.com/a/4060259
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def PrintStacks(stacksToPrint):
    for y in range(0,len(stacksToPrint[0])):
        for x in range(0,len(stacksToPrint)):
            print(stacksToPrint[x][y], end = '')
        print('')
        


#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2



stacks = [[],[],[]]

with open(os.path.join(__location__, '5_input_stacks.txt')) as stack_input_file:
    for line in stack_input_file:
        
        stackLimit = 3
        if len(line) == 36:                                           # True for puzzle input
            stackLimit = 9
        for i in range(0, stackLimit):
            stacks[i].append(line[1+(i*4)])

        

for stack in stacks:
    del stack[-1]                                                     # Nummern entfernen
PrintStacks(stacks)
            
moves = []
with open(os.path.join(__location__, '5_input_moves.txt')) as moves_input_file:
    for line in moves_input_file:


        result = re.search('move (\d+) from (\d+) to (\d+)', line)
        amount = result.group(1)
        fromStack = result.group(2)
        toStack = result.group(3)


        #print(amount, fromStack, toStack)
         