""" Practice while loops and debug them """

# initialize my number
my_number = 8675309

# convert my number to a string to iterate over each digit
my_number_str = str(my_number)

# initialize total to store the sum of the digits
total = 0
index = 0

while index < len(my_number_str):
    value: int = int(my_number_str[index])
    total += value

    index += 1


# print the total sum of all digits
    print(f"The sum of all digits in {my_number} is {total}.")
