"""
Player Object
"""

class Player:
    """
    Data Model to maintain the state of play
    """

    # Player status named constants
    CONDEMNED = "condemned"
    HANGED = "hanged"
    PARDONED = "pardoned"

    # The status of the player (CONDEMNED, HANGED or PARDONED)
    status = CONDEMNED
