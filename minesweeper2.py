
#5 by 5 minesweeper grid written out as per instructions
mine_input_old = [["-", "-", "-", "#", "#"],
              ["-", "#", "-", "-", "-"],
              ["-", "-", "#", "-", "-"],
              ["-", "#", "#", "-", "-"],
              ["-", "-", "-", "-", "-"]]

#I decided to add extra function to create a random minesweeper grid which can be adjusted by changing the row and columns values
#Random module is used to give a random block with a 1 in 4 chance of it being a mine and then this is printed 
import random

def random_grid():
    rows = 5
    cols = 5
    grid = []
    for row in range(rows):
        line = []
        for element in range(cols):
            block = random.choice("---#")
            line.append(block)
        grid.append(line)



    for rows in grid:
        for element in rows:
            print(element, end=" ")
        print()
    print()
    return grid

mine_input = random_grid()

#This function is created to take a particular minesweeper block - identified by row and column (r and c) in the mine_input and return either # if it is
#a mine or a number if it is not - the number being the number of adacent mines.

def mine_counter(r, c):
    positions = [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r,c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]
    #positions relative to chosen block are entered into a list of tuples which can be iterated through
    mine_count = 0

    #This for loop runs through each of the positions relative to the chosen block and increases the mine_count if a mine is detected. The final mine count
    #for this block is returned by the function
    for tup in range(len(positions)):
        if mine_input[r][c] == "#":
            return "#"
        #if the inputted block is # then # is returned by the function
        if 0 <= positions[tup][0] < len(mine_input):
        #if the block is on an edge of a row, any positions from the tuple list of possibilities which have would have be out of bounds or result in [-1]
        # are excluded
            if 0 <= positions[tup][1] < len(mine_input[0]):
        #if the block is on an edge of a column, any positions from the tuple list of possibilities which have would have be out of bounds or result in [-1]
        # are excluded
                if mine_input[positions[tup][0]][positions[tup][1]] == "#":
                    mine_count +=1
                #If the tested position has a # the mine_count increases
    return mine_count


#A new minesweeper grid/nested list is created using list comprehension. The mine_counter function is used to provide the required value for each block

mine_output = [[mine_counter(j, i) for i in range(len(mine_input[0]))] for j in range(len(mine_input))]

#The below code is to print the new mine_output list as a grid
for rows in mine_output:
    for element in rows:
        print(element, end=" ")
    print()
