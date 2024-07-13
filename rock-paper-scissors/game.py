"""
Game Object
"""

import sys
from random import Random

# Possible outcomes of the game
DRAW = "It's a draw!"
PWR = "You win - Paper wraps Rock"
SBR = "I win - Scissors are blunted by Rock"
RWP = "I win - Rock is wrapped by Paper"
SCP = "You win - Scissors cut Paper"
RBS = "You win - Rock blunts Scissors"
PCS = "I win - Paper is cut by Scissors"

# Places the outcomes of the game into a matrix (RPS x RPS)
# where outcome = win_matrix[computer_choice][human_choice]
# Human choice is mapped horizontally
# Computer choice is mapped vertically
OUTCOME_MATRIX = [
    [DRAW, PWR, SBR],
    [RWP, DRAW, SCP],
    [RBS, PCS, DRAW]
]

# Possible choices R, P or S
CHOICES = ["R","P","S"]

class Game:
    """
    The classic game of "Rock, Paper, Scissors"
    """

    def play(self):
        """
        Play the game
        """

        # Write up game instructions
        print("")
        print("=====================")
        print("Rock, Paper, Scissors")
        print("=====================")
        print("")
        print("Enter:")
        print("R for Rock")
        print("P for Paper")
        print("S for Scissors")
        print("")

        # Get the human's choice
        human_choice = self.get_human_choice()

        # Get the computer's choice
        computer_choice = self.get_computer_choice()

        # Evaluate the two choices
        self.check_win(human_choice, computer_choice)

        # End of game
        print("")
        response = input("Press [Enter] to play again, or type Q to quit\n")
        if response.upper() == "Q":
            # End the program
            sys.exit(0)

        # Play again
        self.play()

    def get_human_choice(self):
        """
        Get choice from std input
        """
        # Get user input
        choice = input("What is your choice, human? ").upper()

        # Validate the input to check that it is contained in the list if CHOICES
        try:
            CHOICES.index(choice)
        except ValueError:
            print("Invalid Option: Enter one of R, P or S")
            # Ask agin if validation fails
            return self.get_human_choice()

        # It's a valid choice, so return the choice
        return choice

    def get_computer_choice(self):
        """
        Computer makes a random choice
        """
        # Generate a random integer within the range of CHOICES list (0 - 2)
        index = Random().randint(1, len(CHOICES)) - 1

        # Pick a move based on the random index
        choice = CHOICES[index]

        # Display the computer choice
        print(f"My Choice: {choice}")
        return choice

    def check_win(self, human_choice, computer_choice):
        """
        Find out who wins, or if it is a draw
        """

        # Convert the choices into matrix indices
        human_index = CHOICES.index(human_choice)
        computer_index = CHOICES.index(computer_choice)

        # Output the value from the win matrix for the given choices
        print("")
        print(OUTCOME_MATRIX[computer_index][human_index])
