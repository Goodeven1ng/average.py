# average.py

# Ask the user to enter five numbers
print("Please enter five numbers.")

# Initialize a varible to store sum of numbers
sum = 0

# Get the number from the user and convert it to a float
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())

# Calculate the sum of the numbers
sum = num1 + num2 + num3 + num4 + num5

# Calculate the average of the numbers
average = sum / 5

# Print the average
print(f"The average of those numbers is:\n{average}")