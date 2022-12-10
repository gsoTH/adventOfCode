# https://adventofcode.com/2022/day/8#part2

# Consider each tree on your map. What is the highest scenic score possible for any tree?
    # A tree's scenic score is found by multiplying together its viewing distance in each of the four directions.
    # To measure the viewing distance from a given tree, look up, down, left, and right from that tree; stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. (If a tree is right on the edge, at least one of its viewing distances will be zero.)

import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

trees = []
with open(os.path.join(__location__, '8_input.txt')) as input_file:
    for uncleanLine in input_file:
        line = uncleanLine.strip()
        trees.append(line)

visibleTrees = 0


numRows = len(trees)
numCols = len(trees[0])

maxScore = -1

for row in range(1, numRows-1):
    for col in range(1, numCols-1):
        candidate = trees[row][col]

        distances = [0,0,0,0]

        # look up
        i = row
        while i > 0:
            i -= 1
            distances[0] += 1
            if trees[i][col] >= candidate:
                break
    
        # look down
        for i in range(row+1, numRows):
            distances[1] += 1
            if trees[i][col] >= candidate:
                break

        # look left
        i = col
        while i > 0:
            i-=1
            distances[2] += 1
            if trees[row][i] >= candidate:
                break

        # look right
        for i in range(col+1, numCols):
            distances[3] += 1
            if trees[row][i] >= candidate:
                break

        scenicScore = distances[0] * distances[1] * distances[2] * distances[3]
        if scenicScore > maxScore:
            maxScore = scenicScore


print(maxScore) # 1311 --> too low