"""
Game Object
"""

from getpass import getpass

from player import Player
from board import Board

class Game:
    """
    The classic game of Hangman
    """

    def __init__(self):
        self.player = Player()
        self.board = Board()
        self.word = ""
        self.guess = ""
        self.failed = ""

    def play(self):
        """
        Play the game
        """

        # Get the word to guess from user input
        Board.clear_screen()
        print("Hangman!")
        print("")
        self.word = getpass("Enter your word: ").upper()

        # Set up the start of the game
        self.player.status = Player.CONDEMNED
        self.failed = ""
        self.guess = ""
        for _ in range(len(self.word)):
            self.guess += "_"

        # Main Loop - keep playing until the player is either HANGED or PARDONED
        while self.player.status == Player.CONDEMNED:
            self.board.draw_board(self)
            letter = self.get_user_guess()
            self.update_with_guess(letter)
            self.check_win()

        self.board.draw_board(self)

        # The condemned has won!
        if self.player.status == Player.PARDONED:
            print("Congratulations! you have been pardoned for your crimes. You are now free!")

        # The hangman has won!
        if self.player.status == Player.HANGED:
            print("Your dead mate!")

        # Play another game
        print("")
        input("Press Enter to play again")
        self.play()

    def get_user_guess(self):
        """
        Ask the condemned to make a guess
        """
        letter = input("Condemned - enter one letter: ").upper()
        if len(letter) > 1:
            print("Enter only 1 character")
            return self.get_user_guess()

        if not letter.isalpha():
            print("Enter a letter from the alphabet:")
            return self.get_user_guess()

        if self.failed.find(letter) >= 0 or self.guess.find(letter) >= 0:
            print("You have already guessed that letter")
            return self.get_user_guess()

        return letter

    def update_with_guess(self, letter):
        """
        Update the model with the given user guessed letter
        """
        # Check if the letter is in the word
        position = self.word.find(letter)
        if position >= 0:
            # Correct Guess
            self.populate_guess(letter)
        else:
            # Wrong Guess
            self.populate_failed(letter)

    def populate_failed(self, letter):
        """
        Append a wrongly guessed letter to the failed string
        """
        self.failed += letter

    def populate_guess(self, letter):
        """
        Populate the guess with the correctly guessed letter
        """
        # Find the first position index of the letter in the word we are trying to guess
        start = self.word.find(letter, 0)
        # Continue if it's found
        while start >= 0:
            # Inject the letter at discovered position index
            self.guess = self.guess[:start] + letter + self.guess[start+1:]
            # Check to see if there are any more instances
            start = self.word.find(letter, start+1)

    def check_win(self):
        """
        Check the model to determine if the game is over - either way
        """
        # If the guess and the word are the same, the condemned has been pardoned
        if self.guess == self.word:
            self.player.status = Player.PARDONED

        # If the number of failed attempts is equal to the last frame index
        # of the gallows, the player has been hanged
        if len(self.failed) == Board.get_number_of_frames_of_gallows() - 1:
            self.player.status = Player.HANGED
