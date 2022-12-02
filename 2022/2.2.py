# https://adventofcode.com/2022/day/2#part2

# --- Part Two ---
# The Elf finishes helping with the tent and sneaks back over to you. 
# "Anyway, the second column says how the round needs to end: 
# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win. Good luck!"
sum = 0

with open('2_input.txt') as input_file:
    for line in input_file:
        cleanLine = line.strip()        # Remove a Newline Character From the String 
        chars = cleanLine.split(' ')
        match chars[0]:
            case 'A':
                print('Rock')
            case 'B': 
                print('Paper')
            case 'C':
                print('Scissors')
        match chars[1]:
            case 'X':
                print('Rock')
                sum = sum + 1
                match chars[0]:
                    case 'A':
                        print('draw')
                        sum = sum + 3
                    case 'B': 
                        print('lost')
                        sum = sum + 0
                    case 'C':
                        print('won')
                        sum = sum + 6
            case 'Y': 
                print('Paper')
                sum = sum + 2
                match chars[0]:
                    case 'A':
                        print('won')
                        sum = sum + 6
                    case 'B': 
                        print('draw')
                        sum = sum + 3
                    case 'C':
                        print('lost')
                        sum = sum + 0
            case 'Z':
                print('Scissors')
                sum = sum + 3
                match chars[0]:
                    case 'A':
                        print('lost')
                        sum = sum + 0
                    case 'B': 
                        print('won')
                        sum = sum + 6
                    case 'C':
                        print('draw')
                        sum = sum + 3

print(sum)

