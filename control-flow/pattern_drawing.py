# pattern_drawing.py

# Prompt user for input
size = int(input("Enter the size of the pattern:"))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns (asterisks in each row)
    for col in range(size):
        print("*", end="")  # Print without newline
    print()  # Move to the next line after each row
    row += 1
