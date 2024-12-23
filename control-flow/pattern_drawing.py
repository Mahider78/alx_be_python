# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through rows
row = 0
while row < size:
    # Use a for loop to print '*' in each row
    for col in range(size):
        print("*", end="")
    # Move to the next row after printing all columns
    print()
    row += 1
