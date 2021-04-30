# 8-Tile Puzzle
## How to Run
Run the program using the command: ```python main_menu.py```

A menu will then ask user to choose whether they want to input a custom matrix or use the default matrix provided by the program. The options are '1' and '2'.

After choosing a matrix, the program will ask the user which algorithm they would like to use to solve the problem. The options are:
* 1 - Uniform Cost Search
* 2 - A* with Misplaced Tile Heuristic
* 3 - A* with Euclidean Distance Heuristic

If anything else other than the available choices are inputted, the program will output "You crashed the game!" and exit. Then you will need to start the program again
by running the command provided at the top.

## Files
* ```main_menu.py``` - contains the menu/UI
* ```problem.py``` - the main driver of the program that includes the Problem and Node classes, as well as all three search algorithms
* ```trace_of_sample_matrix.txt```- the solution trace for running the A* with Euclidean Distance Heuristic algorithm on the sample matrix provided on the project specs
