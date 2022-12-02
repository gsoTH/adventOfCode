# https://adventofcode.com/2022/day/2#part2

# --- Part Two ---
# The Elf finishes helping with the tent and sneaks back over to you. 
# "Anyway, the second column says how the round needs to end: 
# X means you need to lose, 
# Y means you need to end the round in a draw, and 
# Z means you need to win. Good luck!"

# Points:
#   1 for Rock, 2 for Paper, and 3 for Scissors
#   0 if you lost, 3 if the round was a draw, and 6 if you won

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
                print('lose')
                sum = sum + 0
                match chars[0]:
                    case 'A':
                        print('Scissors')
                        sum = sum + 3
                    case 'B': 
                        print('Rock')
                        sum = sum + 1
                    case 'C':
                        print('Paper')
                        sum = sum + 2
            case 'Y': 
                print('draw')
                sum = sum + 3
                match chars[0]:
                    case 'A':
                        print('Rock')
                        sum = sum + 1
                    case 'B': 
                        print('Scissors')
                        sum = sum + 3
                    case 'C':
                        print('Paper')
                        sum = sum + 2
            case 'Z':
                print('win')
                sum = sum + 6
                match chars[0]:
                    case 'A':
                        print('Paper')
                        sum = sum + 2
                    case 'B': 
                        print('Scissors')
                        sum = sum + 3
                    case 'C':
                        print('Rock')
                        sum = sum + 1

print(sum)

