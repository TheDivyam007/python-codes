# Get the number of rows and columns for the rectangle
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Loop through each row
for i in range(rows):
    # Loop through each column in the current row
    for j in range(columns):
        # Print a dot without moving to the next line
        print(".", end="")
    # Move to the next line after printing all columns in the current row
    print()
