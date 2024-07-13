"""
Board Object
"""

import os
import platform

BOARD_TEMPLATE =  "   | A | B | C |\n" \
                + "---+---+---+---+\n" \
                + " 1 |   |   |   |\n" \
                + "---+---+---+---+\n" \
                + " 2 |   |   |   |\n" \
                + "---+---+---+---+\n" \
                + " 3 |   |   |   |\n" \
                + "---+---+---+---+\n"

COUNTERS = ['0', 'X']
EMPTY = ' '

class Board:
    """
    Object to handle screen rendering operations
    """

    def __init__(self):
        self.state = []

    def reset(self):
        """
        Reset the board state to all empty!
        """
        self.state = [
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]

    def draw_board(self):
        """
        Draw the current state of play based on the given model
        """
        Board.clear_screen()

        board = BOARD_TEMPLATE
        for column in range(0,3):
            for row in range(0,3):
                position = self.get_position_for_column_row(column, row)
                counter = self.state[row][column]
                board = board[:position] + counter + board[position+1:]
        print(board)

    def convert_coordinates(self, column, row):
        """
        Convert user input coordinates to 0 indexed numeric cartesian coordinates
        """
        c = ['A','B','C'].index(column.upper())
        r = ['1','2','3'].index(row.upper())
        return c, r

    def get_position_for_column_row(self, column, row):
        """
        Map the column/row coordinates to the board string position
        Each row is 16 chars + linebreak (17)
        """
        row_offset = ((row * 2) + 2) * 17
        col_offset = (column * 4) + 5
        return row_offset + col_offset

    def update_board(self, player, column, row):
        """
        Populate the model with the move
        """
        self.state[row][column] = COUNTERS[player - 1]

    def counter_to_player(self, counter):
        """
        Convert a given counter character into a player number
        """
        return COUNTERS.index(counter) + 1

    @staticmethod
    def clear_screen():
        """
        Clear the terminal screen
        """
        if platform.system() == "Windows":
            # Windows
            os.system('cls')
        else:
            # *nix systems
            os.system('clear')

    @staticmethod
    def empty():
        """
        Return the empty constant
        """
        return EMPTY
