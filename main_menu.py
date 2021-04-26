import problem

def main_menu():
    # Need to chagne it a little to ensure user dont put wild inputs
    print('Welcome to 861279550 8 puzzle solver.')
    puzzle_type = input('Type "1" to use a default puzzle, or "2" to enter your own puzzle:\n')

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,0]
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
    algo_choice = input('Uniform Cost Search\nA* with the Misplaced Tile heuristic\nA* with the Euclidian distance heuristic\n')

    puzzle = problem.Problem(matrix)
    #based on algo_choice, call respective search function
    if algo_choice == '1':
        node = problem.ucs(puzzle)
    elif algo_choice == '2':
        node = problem.misplaced(puzzle)
    elif algo_choice == '3':
        node = problem.heuristic(puzzle)
    else:
        print("You crashed the game!")
        return

    # test = problem.Problem(matrix)
    # problem.print_state(test.puzzle)
    # print('\n')
    # # print(test.blank_x, test.blank_y)
    # test.go_up()
    # problem.print_state(test.puzzle)
    # print('\n')
    # test.go_down()
    # problem.print_state(test.puzzle)
    # print('\n')
    # test.go_left()
    # problem.print_state(test.puzzle)
    # print('\n')
    # test.go_right()
    # problem.print_state(test.puzzle)
    # print('\n')
    # test.go_right()
    # problem.print_state(test.puzzle)
    # print(x)
    # x.go_up()
    # print(x)
    # print(problem.find_zero(matrix))
    # problem.print_state(x.init_state.puzzle)
    # print('Problem\'s initial state:', x.init_state.puzzle)
    # print('Problem\'s goal state:', x.goal_state.puzzle)

main_menu()
