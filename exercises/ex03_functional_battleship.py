"""EXO3 - Functional Battleship!"""

__author__ = "730373934"

import random


def input_guess(size: int, spec: str) -> int:
    """Asks the user for a guess of a row or column within the grid size and specification."""
    assert spec == "row" or spec == "column", "Specification must be either 'row' or 'column'"
    
    if spec == "row":
        prompt = "Guess a row: "
    else:
        prompt = "Guess a column: "
    
    while True:
        try:
            guess = int(input(prompt))
            if 1 <= guess <= size:
                return guess  # directly return the user input
            else:
                print(f"The grid is only {size} by {size}. Try again: ", end="")
        except ValueError:
            print("Please enter a valid integer.")


# constants for the colored emoji boxes
BLUE_BOX = "\U0001F7E6"
RED_BOX = "\U0001F7E5"
WHITE_BOX = "\U00002B1C"


def print_grid(size: int, row_guess: int, column_guess: int, is_correct: bool) -> None:
    """Prints the grid with the current guess and updates based on whether it's correct."""
    for row in range(1, size + 1):
        for column in range(1, size + 1):
            if row == row_guess and column == column_guess:
                print(RED_BOX if is_correct else WHITE_BOX, end='')  # no extra spaces between symbols
            else:
                print(BLUE_BOX, end='')  # makes sure BLUE_BOX symbol is correctly used
        print()  # new line after each row, no extra spaces


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Determines if the player's guess matches the secret coordinates."""
    return secret_row == row_guess and secret_column == column_guess


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """The main function to run the game loop used to track the game state and user guesses."""
    turns_left = 5  # Total number of turns allowed.
    for turn in range(1, turns_left + 1):
        print(f"=== Turn {turn}/{turns_left} ===")  # correctly formats turns.
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        
        is_correct = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, is_correct)
        
        if is_correct:
            print("Hit!")  # Use the exact phrase for hits.
            print(f"You won in {turn}/{turns_left} turns!")  # correctly formats wins.
            break  # End the game immediately after a correct guess.
        else:
            print("Miss!")  # Use the exact phrase for misses.
            if turn == turns_left:  # Check if this is the last turn.
                print(f"X/{turns_left} - Better luck next time!")  # correctly formats losses.


# makes python program executable as a script
if __name__ == "__main__":
    grid_size = random.randint(3, 5)  # Randomly determine the grid size between 3x3 and 5x5
    # Adjusted the random.randint calls
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))