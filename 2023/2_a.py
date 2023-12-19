# https://adventofcode.com/2023/day/2
# Determine which games would have been possible if the bag had been loaded with only 
# 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?

test_string = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
with open("2.txt") as file:
    test_data: list[str] = file.readlines()

# test_data: list[str] = test_string.split("\n")



limits: dict = {"red":12, "green": 13, "blue": 14}

sum_valid_game_numbers: int = 0

for line in test_data:
    game_is_possible: bool = True
    if line == "":
        continue
    game: list[str] = line.split(": ")
    game_number: int = int(game[0][5:])
    print(game_number)
    sets: list[str] = game[1].strip().split("; ")   # strip() entfernt "\n"
    for set in sets:
        print(set)
        pairs = set.split(", ")
        for pair in pairs:
            print(pair)
            data: list[str] = pair.split(" ")
            number: int = int(data[0])
            colour: str = data[1]
            limit = limits.get(colour)
            if  limit < number:
                game_is_possible = False

    if game_is_possible:
        sum_valid_game_numbers += game_number

print(sum_valid_game_numbers)
            

    