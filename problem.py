import sys
import math
from copy import deepcopy

_max = sys.maxsize

expanded_children = 0
max_q_size = 0

# ---------------------- Problem Class ----------------------  #
class Problem:
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
        else:
            return False

    # 0 in last row -> cannot go down
    def go_down(self):
        if 0 not in self.puzzle[2]:
            # Wherever 0 is, the only thing that changes is its x (col) position +1
            self.swap_tile(self.blank_x + 1, self.blank_y)
            self.blank_x += 1
            return True
        else:
            return False

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
# ------------------------------------------------------------------------------ #


# ---------------------- Node Class ----------------------  #
class Node:

    def __init__(self, problem, path_cost, heuristic_cost):
        self.problem = problem
        self.path_cost = path_cost
        self.heuristic_cost = heuristic_cost

    def create_child(node):
        # Need a deep copy because we have a list of list
        # Also, we don't want it to reference the og copy
        new_child = deepcopy(node)
        new_child.path_cost += 1
        return new_child

    def expand(node):
        global expanded_children
        new_children = []

        # Check whether an operation was successfully applied
        if node.problem.go_up():
            new_children.append(Node.create_child(node))
            node.problem.go_down() # Undo the move so the next operation can be applied
        if node.problem.go_down():
            new_children.append(Node.create_child(node))
            node.problem.go_up()
        if node.problem.go_left():
            new_children.append(Node.create_child(node))
            node.problem.go_right()
        if node.problem.go_right():
            new_children.append(Node.create_child(node))
            node.problem.go_left()
        
        # expanded_children += len(new_children)
        expanded_children += 1
        return new_children

    # Need to choose a leaf node that has the least cost to remove and expand next
    def deque(nodes):
        lowest_cost = _max
        node_to_remove = nodes[0]
        for node in nodes:
            if (node.path_cost + node.heuristic_cost) < lowest_cost:
                lowest_cost = node.path_cost + node.heuristic_cost
                node_to_remove = node
        nodes.remove(node_to_remove)
        return node_to_remove
# ------------------------------------------------------------------------------ #


# ---------------------- Helper Functions ----------------------  #
def print_state(matrix):
    for row in matrix:
        print(*row, sep=' ')

def find_zero(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                return  x, y

def contain(node, nodes):
    for i in range(len(nodes)):
        if node.problem.puzzle == nodes[i].problem.puzzle:
            return True
    return False
# ------------------------------------------------------------------------------ #

# function GRAPH-SEARCH(problem) returns a solution, or failure
#     initialize the frontier using the initial state of problem
#     initialize the explored set to be empty
#     loop do
#         if the frontier is empty then return failure
#         choose a leaf node and remove it from the frontier
#         if the node contains a goal state then return the corresponding solution
#         add the node to the explored set
#         expand the chosen node, adding the resulting nodes to the frontier
#             only if not in the frontier or explored set

# ---------------------- Uniform Cost Search ----------------------  #
def ucs(problem):
    global max_q_size
    node = Node(problem, 0, 0)
    # initialize the frontier using the initial state of problem
    frontier = [node]
    # initialize the explored set to be empty
    explored_set = []

    # loop do
    while True:
        max_q_size = max(len(frontier), max_q_size)
        # if the frontier is empty then return failure
        if not bool(frontier):
            return [], expanded_children, max_q_size

        # choose a leaf node and remove it from the frontier
        node = Node.deque(frontier)
        # if the node contains a goal state then return the corresponding solution
        if node.problem.puzzle == node.problem.goal_state:
            return node, expanded_children, max_q_size

        print('The best state to expand with a g(n) = ', node.path_cost, 'and h(n) = 0 is...')
        print_state(node.problem.puzzle)
        print('\tExpanding this node...\n')
        # add the node to the explored set
        explored_set.append(node)
        # expand the chosen node, adding the resulting nodes (new children) to the frontier
        new_children_nodes = Node.expand(node)
        for child in new_children_nodes:
            in_expand_list = contain(child, frontier)
            in_explored_list = contain(child, explored_set)
            # only if not in the frontier or explored set
            if not in_expand_list and not in_explored_list:
                frontier.append(child)
# ------------------------------------------------------------------------------ #
    

# ---------------------- A* with Misplaced Tile Heuristic ----------------------  #
def find_misplaced_heuristic(node):
    num_misplaced = 0
    for row in range(len(node.problem.puzzle)):
        for col in range(len(node.problem.puzzle[row])):
            if node.problem.puzzle[row][col] != node.problem.goal_state[row][col]:
                # The blank can't really be a "misplaced" tile, only the elem that the blank space took over
                if node.problem.puzzle[row][col] != 0:
                    num_misplaced += 1
    return num_misplaced

def misplaced(problem):
    global max_q_size
    node = Node(problem, 0, 0)
    frontier = [node]
    explored_set = []

    node.heuristic_cost = find_misplaced_heuristic(node)

    while True:
        max_q_size = max(len(frontier), max_q_size)
        # frontier is empty -> fail
        if not bool(frontier):
            return [], 0, 0

        # Choose the next node
        node = Node.deque(frontier)
        if node.problem.puzzle == problem.goal_state:
            return node, expanded_children, max_q_size
        print('The best state to expand with a g(n) =', node.path_cost, 'and h(n) =', node.heuristic_cost, 'is...')
        print_state(node.problem.puzzle)
        print('\tExpanding this node...\n')
        explored_set.append(node)
        new_children_nodes = Node.expand(node)
        for child in new_children_nodes:
            child.heuristic_cost = find_misplaced_heuristic(child)
            in_expand_list = contain(child, frontier)
            in_explored_list = contain(child, explored_set)
            if not in_expand_list and not in_explored_list:
                frontier.append(child)
# ------------------------------------------------------------------------------ #


# ---------------------- A* with Euclidean Distance Heuristic ----------------------  #        
def find_correct_position(puzzle, val):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == val:
                return i,j

def calc_euclidean_heuristic(node):
    curr_node = node.problem.puzzle
    goal_state = node.problem.goal_state
    eucl_heuristic_sum = 0
    for x1 in range(len(curr_node)):
        for y1 in range(len(curr_node[x1])):
                if curr_node[x1][y1] != 0 and curr_node[x1][y1] != goal_state[x1][y1]:
                    (x2, y2) = find_correct_position(goal_state, curr_node[x1][y1])
                    eucl_heuristic_sum += math.ceil(math.sqrt(pow(x2 - x1,2) + pow(y2 - y1, 2)))
    return eucl_heuristic_sum

def euclidean(problem):
    global max_q_size
    node = Node(problem, 0, 0)
    frontier = [node]
    explored_set = []

    node.heuristic_cost = calc_euclidean_heuristic(node)

    while True:
        max_q_size = max(len(frontier), max_q_size)
        # frontier is empty -> fail
        if not bool(frontier):
            return [], 0, 0

        # Choose the next node
        node = Node.deque(frontier)
        if node.problem.puzzle == problem.goal_state:
            return node, expanded_children, max_q_size
        print('The best state to expand with a g(n) =', node.path_cost, 'and h(n) =', node.heuristic_cost, 'is...')
        print_state(node.problem.puzzle)
        print('\tExpanding this node...\n')
        explored_set.append(node)
        new_children_nodes = Node.expand(node)
        for child in new_children_nodes:
            child.heuristic_cost = calc_euclidean_heuristic(child)
            in_expand_list = contain(child, frontier)
            in_explored_list = contain(child, explored_set)
            if not in_expand_list and not in_explored_list:
                frontier.append(child)