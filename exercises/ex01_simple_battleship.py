"""EXO1 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730373934"

# Importing the exit function
from sys import exit

# asking user to pick secret boat location
boat_location = int(input("Pick a secret boat location between 1 and 4: "))

# checking if input is valid
if boat_location < 1:
    print(f"Error! {boat_location} too low!")
    exit()
elif boat_location > 4:
    print(f"Error! {boat_location} too high!")
    exit()

# asking second user to guess the number
guess = int(input("Guess a number between 1 and 4: "))
if guess < 1:
    print(f"Error! {guess} too low!")
    exit()
elif guess > 4:
    print(f"Error! {guess} too high!")
    exit()

# named variables for emojis
blue_box = "\U0001F7E6"
red_box = "\U0001F7E5"
white_box = "\U00002B1C"

# determining result box color
result_box = red_box if guess == boat_location else white_box

# initializing the emoji string of boxes
emoji_string = ""

# building emoji string of boxes
for position in range(1, 5):
    if position == guess:
        emoji_string += result_box
    else:
        emoji_string += blue_box

# print emoji string of boxes
print(emoji_string)

# checking if guess (from 2nd player) is correct
if guess == boat_location:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")
