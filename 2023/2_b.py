# https://adventofcode.com/2023/day/2
# The power of a set of cubes is equal to the numbers of red, green, and blue 
# cubes multiplied together. The power of the minimum set of cubes in game 1 
# is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up 
# these five powers produces the sum 2286.
#
# For each game, find the minimum set of cubes that must have been present. 
# What is the sum of the power of these sets?

test_string = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
with open("2.txt") as file:
    test_data: list[str] = file.readlines()

#test_data: list[str] = test_string.split("\n")





sum_valid_game_numbers: int = 0

for line in test_data:
    if line == "":
        continue
    game: list[str] = line.split(": ")
    game_number: int = int(game[0][5:])
    print(game_number)
    sets: list[str] = game[1].strip().split("; ")   # strip() entfernt "\n"
    fields = ["red", "green", "blue"]
    upper_bounds = [  0, 0, 0]
    for set in sets:
        print(set)
        pairs = set.split(", ")
        for pair in pairs:
            print(pair)
            data: list[str] = pair.split(" ")
            number: int = int(data[0])
            colour: str = data[1]
            for i in range(len(fields)):
                if colour == fields[i]:
                    if upper_bounds[i] < number:
                        upper_bounds[i] = number
    power: int = upper_bounds[0] * upper_bounds[1] * upper_bounds[2]
    sum_valid_game_numbers += power


print(sum_valid_game_numbers)
            

    