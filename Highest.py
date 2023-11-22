# Function to get input marks from the user
def get_user_marks():
    marks = []
    for i in range(5):
        while True:
            try:
                mark = float(input(f"Enter mark {i + 1}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return marks

# Function to find and display the highest mark
def display_highest_mark(marks):
    highest_mark = max(marks)
    print(f"The highest mark is: {highest_mark}")

# Main program
if __name__ == "__main__":
    # Get input marks from the user
    user_marks = get_user_marks()

    # Display the highest mark
    display_highest_mark(user_marks)
