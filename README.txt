
Do you want to solve one maze or multiple mazes while reading from the text file? You are in the right place. 

-Starting the program
-- To start the program we simply need place input.txt and maze.py in the same directory and run the python code
-- If you interested in creating your own maze/mazes, use mazegeneration.py to create your own mazes. 
   ---To create your own maze, open the linux terminal and type the command: python mazegeneration.py (NUM) >> output.txt from the directory where maze generation.py is located
   ---Above command will keep appending mazes to output.txt. Here NUM refers to size of row and column which is a positive integer
   ---After creating mazes copy your txt file in the same directory as maze.py and change line 20 of code to change name of file to 'output.txt'

-Description of Program internals

--Description of methods-

---The program has six methods namely, read_all_mazes_from_file(), solve_one_maze(), error_in_maze(), error_in_size(),finds_path(row,  column), and print_maze().

--- read_all_mazes_from_file()- Reads all the lines from a file, breaks down lines to one line if line has character length of 1, which is just '\n' then  solves
--- the maze currently stored. Else, keeps adding the line from a file to maze array-list

--- solve_one_maze()- Solves one maze if there are no errors. If there is no solution, prints out 'No Solution'

--- error_in_maze()- If the maze has any other character except '+', '-', '|' or '\n' returns true

--- error_in_size()- If  column or  row of the maze has more than 150 characters returns true

--- finds_path(row,  column)- This function solves the maze recursively using starting point and finds finishing path using max_row and max_column
--- returns true if it finds the path to the finish line, else returns false, prints path with '*' and trails with 'H'. The finish line is denoted by 'F'

--- print_maze()- Prints one maze after solving the maze. Removes trials denoted by character 'H' and replaces Finish Line 'F' with '*'



--Algorithm Details

--- Recursive Algorithm used in finds_path(row,  column)-  * > Recursively checks in all four direction from the starting point
 							   * > if finds empty character in any one of the four direction, keeps checking
 							   *    recursively from that co-ordinate until it finds Finish line and returns true
 							   * > if it does not find empty character in all four direction, returns false


-Known Bugs and feature requests-
--1) The program could have been more robust in terms of reading mazes. At the moment, the program can only read maze generated from mazegeneration.py
--2) The program could have asked the user which maze to solve from all the mazes. The program is not user friendly and directly solves the problem
--3) The program could have written the output in the text file after solving the problem



-References-

---1)	https://www.cs.bu.edu/teaching/alg/maze/
---2)   http://rosettacode.org/wiki/Maze_generation#Python
---3)   https://stackoverflow.com/questions/42168317/how-to-create-two-dimensional-list-of-characters-from-file
---4)   https://stackoverflow.com/questions/23799036/how-to-traverse-a-2d-list-in-python
---5)   https://stackoverflow.com/questions/8177079/python-take-the-content-of-a-list-and-append-it-to-another-list
---6)   https://www.w3schools.com/python/python_conditions.asp


-Author - Amun Kharel
-Date - 03/23/2019