"""
Game Object
"""

from board import Board

NOBODY = 0

class Game:
    """
    The classic game of Noughts and Crosses
    """

    def __init__(self):
        self.board = Board()
        self.player = 1
        self.winner = NOBODY
        self.turns_taken = 0

    def play(self):
        """
        Play the game
        """

        # Initialise the game
        self.player = 1
        self.winner = NOBODY
        self.turns_taken = 0
        self.board.reset()

        # Keep Looping as long as nobody has won
        while self.winner is NOBODY and self.turns_taken < 9:
            self.board.draw_board()
            self.player_turn()
            self.turns_taken += 1

        self.board.draw_board()

        # Prize giving ceremony
        if self.winner is not NOBODY:
            print(f"Player %d wins!" % self.winner)
        else:
            print("Stalemate!")


        # Play another game
        print("")
        input("Press Enter to play again")
        self.play()

    def player_turn(self):
        """
        Ask the player to move
        """
        move = input(f"Player %d - make your move: " % self.player).upper()

        # Validate the move
        try:
            column, row = self.board.convert_coordinates(move[0].upper(), move[1].upper())
        except (ValueError, IndexError):
            print("Enter 2 characters [COLUMN][ROW] - example: C3")
            return self.player_turn()

        if  self.board.state[row][column] is not Board.empty():
            print("That cell is already taken")
            return self.player_turn()
        
        # Update the board
        self.board.update_board(self.player, column, row)

        # Has someone won or is there a draw?
        self.check_win()

        # Flip the player turn
        # This is simple and efficient way of flipping between 1 & 2
        self.player = 3 - self.player

    def check_win(self):
        """
        Is the game over?
        """
        # Check vertical lines
        for column in range(0,3):
            r1 = self.board.state[0][column]
            win_col = r1 != Board.empty()
            for row in range(1,3):
                if self.board.state[row][column] == r1:
                    win_col = win_col & True
                else:
                    win_col = False

            if win_col is True:
                self.winner = self.board.counter_to_player(r1)

        # Check horizontal lines
        for row in range(0,3):
            r1 = self.board.state[row][0]
            win_row = r1 != Board.empty()
            for column in range(1,3):
                if self.board.state[row][column] == r1:
                    win_row = win_row & True
                else:
                    win_row = False

            if win_row is True:
                self.winner = self.board.counter_to_player(r1)

        # Check diagonal lines
        r1 = self.board.state[0][0] # TL -> BR
        r2 = self.board.state[2][0] # TR -> BL
        win_d1 = r1 != Board.empty()
        win_d2 = r2 != Board.empty()
        for column in range(1,3):
            if self.board.state[column][column] == r1:
                win_d1 = win_d1 & True
            else:
                win_d1 = False

            if self.board.state[2-column][column] == r2:
                win_d2 = win_d2 & True
            else:
                win_d2 = False

        if win_d1 is True:
            self.winner = self.board.counter_to_player(r1)

        if win_d2 is True:
            self.winner = self.board.counter_to_player(r2)
