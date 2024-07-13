"""
Board Object
"""

import os
import platform

# Array of ASCII graphical frames for rendering the gallows
GALLOWS = [
    "\n\n\n\n\n\n\n",
    "\n\n\n\n\n\n\n----------",
    "   \n  |\n  |\n  |\n  |\n  |\n  |\n----------",
    "   _____\n  |\n  |\n  |\n  |\n  |\n  |\n----------",
    "   _____\n  | /\n  |/\n  |\n  |\n  |\n  |\n----------",
    "   _____\n  | /   |\n  |/\n  |\n  |\n  |\n  |\n----------",
    "   _____\n  | /   |\n  |/    O\n  |\n  |\n  |\n  |\n----------",
    "   _____\n  | /   |\n  |/    O\n  |     |\n  |\n  |\n  |\n----------",
    "   _____\n  | /   |\n  |/    O\n  |    /|\n  |\n  |\n  |\n----------",
    "   _____\n  | /   |\n  |/    O\n  |    /|\\\n  |\n  |\n  |\n----------",
    "   _____\n  | /   |\n  |/    O\n  |    /|\\\n  |    /\n  |\n  |\n----------",
    "   _____\n  | /   |\n  |/    O\n  |    /|\\\n  |    / \\\n  |\n  |\n----------",
]

class Board:
    """
    Object to handle screen rendering operations
    """

    def draw_board(self, game):
        """
        Draw the current state of play based on the given model
        """
        Board.clear_screen()

        # Show the current correctly guessed letters in their positions
        print(game.guess)

        # The frame to show is based on the number of failed guesses
        print(GALLOWS[len(game.failed)])

        # Show the failed guesses
        print("")
        print(game.failed)
        print("")

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
    def get_number_of_frames_of_gallows():
        """
        Return a count of the number of frames in the gallows
        """
        return len(GALLOWS)
