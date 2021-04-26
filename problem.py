# This generates the whole solution
    # Starting with init_state
    # For every operator generate a new state - This is using the algorithm?
    # If the state we arrive at matches the goal state then we found the solution

# import node
import sys

_max = sys.maxsize

expanded_children = 0
children_to_expand = [] #frontier

class Problem:
    #curr_state = [] # changed from init_state
    goal_state = [
        [1,2,3],
        [4,5,6],
        [7,8,0]
    ]

    def __init__(self, matrix):
        self.puzzle = matrix
        self.blank_x, self.blank_y = find_zero(matrix)
    
    # 0 in 1st row -> cannot go up
    def go_up(self):
        if 0 not in self.puzzle[0]:
            # Wherever 0 is, the only thing that changes is its x (col) position -1
            self.swap_tile(self.blank_x - 1, self.blank_y) # col = x axis, row = y axis
            self.blank_x -= 1
            return True

    # 0 in last row -> cannot go down
    def go_down(self):
        if 0 not in self.puzzle[2]:
            # Wherever 0 is, the only thing that changes is its x (col) position +1
            self.swap_tile(self.blank_x + 1, self.blank_y)
            self.blank_x += 1
            return True

    # 0 in 1st col -> cannot go left
    def go_left(self):
        can_go_left = True
        for row in self.puzzle:
            if row[0] == 0:
                can_go_left = False
        if can_go_left:
            self.swap_tile(self.blank_x, self.blank_y - 1)
            self.blank_y -= 1
            return True
        else:
            return False

    # 0 in last col -> cannot go right
    def go_right(self):
        can_go_right = True
        for row in self.puzzle:
            if row[2] == 0:
                can_go_right = False
        if can_go_right:
            self.swap_tile(self.blank_x, self.blank_y + 1)
            self.blank_y += 1
            return True
        else:
            return False

    def swap_tile(self, new_x, new_y):
        temp = self.puzzle[self.blank_x][self.blank_y]
        self.puzzle[self.blank_x][self.blank_y] = self.puzzle[new_x][new_y]
        self.puzzle[new_x][new_y] = temp

class Node:
    # Construct a state, which is a node
    # def __init__(self, row1, row2, row3):
    #     self.puzzle_state = [row1, row2, row3]

    def __init__(self, problem, path_cost, heuristic_cost):
        self.puzzle = problem
        self.parent = []
        self.path_cost = path_cost
        self.heuristic_cost = heuristic_cost

    # expand node



# Helpers
def print_state(matrix):
    for row in matrix:
        print(*row, sep=' ')

def find_zero(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                return  x, y

def pop_node(nodes):
    lowest_cost = _max
    index_node_to_pop = 0
    for index in range(len(nodes)):
        if (nodes[index].path_cost + nodes[index].heuristic_cost) < lowest_cost:
            lowest_cost = (nodes[index].path_cost + nodes[index].heuristic_cost)
    return nodes[index_node_to_pop], index_node_to_pop

def ucs(problem):
    node = Node(problem.puzzle, 0, 0)
    frontier = [node]

    # frontier is empty -> failed
    if not bool(frontier):
        return []

def misplaced(problem):
    print('called misplaced')

def heuristic(problem):
    print('called heuristic')