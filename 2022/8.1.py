# https://adventofcode.com/2022/day/8

# how many trees are visible from outside the grid?

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
visibleTrees -= (numRows*2)         # oberste, unterste Zeile
visibleTrees -= (numCols*2)         # linke, rechte Spalte
visibleTrees += 4                   # Ecken wurden doppelt abgezogen

visibleTrees = numRows*numCols
print(visibleTrees)
num = 0
for row in range(1, numRows-1):
    for col in range(1, numCols-1):
        candidate = trees[row][col]
        isHiddenTop = False
        isHiddenBottom = False
        isHiddenLeft = False
        isHiddenRight = False

        for i in range(0, row):
          if trees[i][col] <= candidate:
            isHiddenTop = True

        for i in range(row+1, numRows):
            if trees[i][col] <= candidate:
                isHiddenBottom = True

        for i in range(0, col):
            if trees[row][i] <= candidate:
                isHiddenLeft = True

        for i in range(col+1, numCols):
            if trees[row][i] <= candidate:
                isHiddenRight = True

        if isHiddenTop and isHiddenBottom and isHiddenLeft and isHiddenRight:
            visibleTrees -= 1
        
        num +=1
        print(num)
    print()    

print(visibleTrees)