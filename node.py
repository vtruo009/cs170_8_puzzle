# Main responsibility is to create a node for a state and nothing else

class Node:
    puzzle = []
    parent = []

    # Construct a state, which is a node
    # def __init__(self, row1, row2, row3):
    #     self.puzzle_state = [row1, row2, row3]

    def __init__(self, matrix):
        self.puzzle = matrix
