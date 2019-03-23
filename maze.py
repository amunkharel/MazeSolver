"""
Program Description:
Reads maze or mazes from a text file generated with mazegeneration.py
and solves each one if there are no errors present

Source of mazegeneration.py- http://rosettacode.org/wiki/Maze_generation#Python

Author: Amun Kharel
Date: 3/23/2019
"""

"""
ArrayList to store one maze from the file
"""
maze = []

"""
Name of the text file (has to be in the same directory)
"""
filename = 'input.txt'


"""
Reads all the lines from a file, breaks down lines to one line
if line has character length of 1, which is just '\n' then  solves
the maze currently stored. Else, keeps adding the line from a file to
maze arraylist

"""
def read_all_mazes_from_file():
    with open(filename, 'r') as f:

        counter = 0

        lines = f.readlines()

        for line in lines:

            if len(line) == 1:
                counter += 1
                if counter == 1:
                    solve_one_maze()
                    maze.clear()

            if len(line) != 1:
                maze.append(list(line))
                counter = 0
    f.close()


"""
Solves one maze if there are no errors
If there is no solution, prints out 'No Solution'
"""

def solve_one_maze():
    if error_in_maze():
        print("Error in the maze \n\n")

    elif error_in_size():
        print("Error in the size \n\n")

    elif finds_path(1, 2):
        print_maze()

    else:
        print("No Solution\n\n")


""" 
If the maze has any other character except '+', '-', '|' or '\n' returns true

 * @return Returns true if error else returns false
"""

def error_in_maze():
    error = None
    for row in maze:
        for item in row:
            if item == '+' or item == '-' or item == ' ' or item == '|' or item == '\n':
                error = False
            else:
                return True
    return error

"""
If  column or  row of the maze has more than 150 characters returns true

 * @return If error in size returns true, else returns false
"""

def error_in_size():

    max_row = len(maze)

    max_column = len(maze[0]) - 1

    if max_row > 150 or max_column > 150:
        return True
    else:
        return False


"""
This function solves the maze recursively using starting point
and finds finishing path using max_row and max_column
returns true if it finds the path to the finish line,
else returns false, prints path with '*' and trails with 'H'.
The finish line is denoted by 'F'
 * @param row, starting row of the maze, that is 1
 * @param column, starting column of maze, that is 2
 * @return, returns True if finds path and False if does not find path

Algorithm researched using https://www.cs.bu.edu/teaching/alg/maze/
Implementation by Author- Amun Kharel
"""
def finds_path(row,  column):
    max_row = len(maze)

    max_column = len(maze[0]) - 1

    maze[max_row - 2][max_column - 3] = 'F'

    if maze[row][column] == 'F':
        return True

    if maze[row][column] == '+' or maze[row][column] == '|' or maze[row][column] == '-' or maze[row][column] == 'H':
        return False

    maze[row][column] = 'H'

    if finds_path(row - 1, column):
        maze[row][column] = '*'
        return True

    if finds_path(row + 1, column):
        maze[row][column] = '*'
        return True

    if finds_path(row, column - 2):
        maze[row][column] = '*'
        return True

    if finds_path(row, column + 2):
        maze[row][column] = '*'
        return True

    return False


"""
Prints one maze after solving the maze
Removes trials denoted by character 'H' and 
replaces Finish Line 'F' with '*'
"""
def print_maze():
    for row in maze:
        for item in row:
            if item == 'H':
                item = ' '

            if item == 'F':
                item = '*'

            print(item, end="")
    print('\n\n')



if __name__ == '__main__':
    read_all_mazes_from_file()
