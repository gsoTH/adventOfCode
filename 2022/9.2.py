# https://adventofcode.com/2022/day/9

# Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
    # addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
    # noop takes one cycle to complete. It has no other effect.

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


instructions = []

with open(os.path.join(__location__, '9_input.txt')) as input_file:
    for uncleanLine in input_file:
        line = uncleanLine.strip()
        cols = line.split(' ')
        
        duration = 1
        amount = 0
        if cols[0] == 'addx':
            duration = 2
            amount = int(cols[1])
        
        
        instruction = []
        instruction.append(duration)
        instruction.append(amount)

        instructions.append(instruction)

relevantCycles = [20, 60, 100, 140, 180, 220]

instructionCounter = 0
x = 1
signalSum = 0
#print('cycle\t iC\t x\t sS\tinstr')
crt = []
text = ''
cycle = 1
while instructionCounter < len(instructions):
    cycle += 1
    instructions[instructionCounter][0]-=1
    instr = instructions[instructionCounter][0]
    sprite = [x-1, x, x+1]
    if len(text) in sprite:
        text = text + '#'
    else:
        text = text + '.'
        
    if len(text) == 40:
        crt.append(text)
        text = ''
    
    if instr == 0:
        x += instructions[instructionCounter][1]
        instructionCounter += 1
    
    
    #print(cycle,'\t', instructions[instructionCounter][1],'\t', x,'\t', signalSum,'\t',instr)

crt.append(text)

for line in crt:
    print(line)
    
        


