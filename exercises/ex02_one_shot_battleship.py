"""EXO2 - One Shot Battleship!"""

__author__ = "730373934"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

row_guess = int(input("Guess a row: "))

while row_guess > grid_size or row_guess < 1:
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_guess = int(input("Guess a column: "))

while column_guess > grid_size or column_guess < 1:
    column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

row_counter = 1

# checking if row position is within grid
while row_counter <= grid_size:
    
    row_string = ""
    column_counter = 1

    # checking if row position is at row guess 
    if row_counter == row_guess:

        # checking if column position is within grid
        while column_counter <= grid_size:
            # checking if column position is at column guess
            if column_counter == column_guess:
                # if correct guess is made
                if row_counter == secret_row and column_counter == secret_column:
                    row_string += RED_BOX
                # if incorrect guess is made; at the guess location
                else:
                    row_string += WHITE_BOX
            # if the column position is not the column guess
            else:
                row_string += BLUE_BOX
            column_counter += 1
    # if the row position is not the row guess
    else:
        # checking if column position is within grid
        while column_counter <= grid_size:
            row_string += BLUE_BOX
            column_counter += 1

    print(row_string)
    row_counter += 1

# Feedback for the user based on their guess
if row_guess == secret_row and column_guess == secret_column:
    print("Hit!")
elif row_guess == secret_row:
    print("Close! Correct row, wrong column.")
elif column_guess == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")