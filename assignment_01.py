# Question 01 and Question 02:
import math
print("WELCOME TO YOUR CALCULATOR!!!")
print("Choose a mathematical operation:")
print("1. Factorial")
print("2. Square Root")
print("3. Exponential (e^x)")

choice = input("Enter your choice (1-3): ")

try:
    number = float(input("Enter a number: "))

    match choice:
        case "1":
            if number < 0 or not number.is_integer():
                print("Factorial is only for non-negative whole numbers.")
            else:
                print(f"Factorial of {int(number)} is: {math.factorial(int(number))}")
        case "2":
            if number < 0:
                print("Square root is not defined for negative numbers.")
            else:
                print(f"Square root of {number} is: {math.sqrt(number)}")
        case "3":
            print(f"e^{number} is: {math.exp(number)}")
        case _:
            print("Invalid choice. Please enter 1, 2, or 3.")

except ValueError:
    print("Invalid number entered.")
# Question 02:
# Imagine you are designing a seating arrangement for a theater. Each row in the theater has a 
# different number of seats. Write a Python program that generates a seating chart for the theater
#  using nested loops. Your program should: Prompt the user to enter the number of rows in the theater.
# For each row, prompt the user to enter the number of seats in that row. Using nested loops, generate and
#  print a seating chart for the theater, where each seat is represented by a number.
# Use appropriate symbols to represent empty seats and occupied seats (e.g., "." for empty seats and "X" 
# for occupied seats).
# Get the number of rows
rows = int(input("Enter the number of rows in the theater: "))
seating_chart = []

# For each row, ask how many seats it has
for i in range(rows):
    seats = int(input(f"Enter number of seats in row {i + 1}: "))
    row = []
    for j in range(seats):
        row.append('.')  # '.' means empty
    seating_chart.append(row)

print("\nSeating Chart:")
for i in range(rows):
    print(f"Row {i + 1}: ", end="")
    for seat in seating_chart[i]:
        print(seat, end=" ")
    print()  # Newline for the next row
