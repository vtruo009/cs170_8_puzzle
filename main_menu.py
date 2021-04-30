import time
import problem

def main_menu():
    # Check whether we need to make synamic size
    print('Welcome to 861279550\'s 8 puzzle solver.')
    puzzle_type = input('Type "1" to use a default puzzle, or "2" to enter your own puzzle:\n')

    matrix = [
        [1,0,3],
        [4,2,6],
        [7,5,8]
    ]

    if puzzle_type == '2':
        print('Enter your puzzle, use a zero to represent the blank')
        row1 = input('Enter the first row, use space or tabs between numbers: ').split(' ')
        matrix[0] = [int(i) for i in row1]
        row2 = input('Enter the second row, use space or tabs between numbers: ').split(' ')
        matrix[1] = [int(i) for i in row2]
        row3 = input('Enter the third row, use space or tabs between numbers: ').split(' ')
        matrix[2] = [int(i) for i in row3]
    elif puzzle_type > '2' or puzzle_type < '1':
        print('You crashed the game!')
        return

    print('Enter your choice of algorithm')
    algo_choice = input('Uniform Cost Search\nA* with the Misplaced Tile heuristic\nA* with the Euclidean Distance heuristic\n')

    puzzle = problem.Problem(matrix)
    print('\n')

    start_time = time.time()
    
    # Based on algo_choice, call respective search function
    if algo_choice == '1':
        print('Starting Uniform Cost Search with:')
        problem.print_state(puzzle.puzzle)
        print('\n')
        (node, expanded_children, max_q_size) = problem.ucs(puzzle)
    elif algo_choice == '2':
        print('Starting A* with the Misplaced Tile heuristic with:')
        problem.print_state(puzzle.puzzle)
        print('\n')
        (node, expanded_children, max_q_size) = problem.misplaced(puzzle)
    elif algo_choice == '3':
        print('Starting A* with the Euclidean Distance heuristic with:')
        problem.print_state(puzzle.puzzle)
        print('\n')
        (node, expanded_children, max_q_size) = problem.euclidean(puzzle)
    else:
        print("You crashed the game!")
        return

    if not bool(node):
        print('No solution was found.')
        return

    print('\nGoal!! Goal state:')
    problem.print_state(node.problem.puzzle)
    print('\nTo solve this problem the search algorithm expanded a total of', expanded_children, 'nodes')
    print('The maximum number of nodes in the queue at any one time:', max_q_size)


    print(time.time() - start_time, 'seconds')


main_menu()