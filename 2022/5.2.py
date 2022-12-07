# https://adventofcode.com/2022/day/5

import os
import re

# Pfade zuverlässig angeben: https://stackoverflow.com/a/4060259
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def PrintStacks():
    for x in range(0,len(stacks)):
        print(x, ': ', end = '')
        for y in range(0,len(stacks[x])):
        
            print(stacks[x][y], end = '')
        print('')
    print('-------------------------------------')

def PrintTopLayer():
    text = ''
    for x in range(0,len(stacks)):
        text = text + stacks[x][0]

    print('Top Layers: ', text)
            


#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2


# Stacks einlesen
stacks = [[],[],[]]
with open(os.path.join(__location__, '5_input_stacks.txt')) as stack_input_file:
    for line in stack_input_file:
        
        stackLimit = 9
        if len(line) < 30:                                           # True for test input
            stackLimit = 3
        while len(stacks) < stackLimit:
            stacks.append([])

        for i in range(0, stackLimit):
            item = line[1+(i*4)]
            if not item == ' ':
                stacks[i].append(item)

        
# Nummern entfernen
for stack in stacks:
    del stack[-1]                                                     
PrintStacks()


# moves einlesen
moves = []
with open(os.path.join(__location__, '5_input_moves.txt')) as moves_input_file:
    for line in moves_input_file:


        result = re.search('move (\d+) from (\d+) to (\d+)', line)      #https://regex101.com/r/CE1LMf/1
        amount = int(result.group(1))
        fromStack = int(result.group(2)) - 1
        toStack = int(result.group(3)) - 1

        print(amount, fromStack, toStack)

        itemsToInsert = []
        for i in range(0, amount):
            itemsToInsert.append(stacks[fromStack][0])
            del stacks[fromStack][0]
        
        itemsToInsert.reverse()
        
        for item in itemsToInsert:
            stacks[toStack].insert(0, item)
        PrintStacks()

PrintTopLayer()
