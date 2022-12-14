# https://adventofcode.com/2022/day/2
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
#
# A Y
# B X
# C Z
#
# This strategy guide predicts and recommends the following:
#   In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
#   In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
#   The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?

# Key:
#   A for Rock, B for Paper, and C for Scissors
#   X for Rock, Y for Paper, and Z for Scissors
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

