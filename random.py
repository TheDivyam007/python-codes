# Import the random module to generate random numbers
import random

# Function to take 5 random numbers from the user
def get_random_numbers():
    random_numbers = []
    for _ in range(5):
        num = int(input("Enter a random number: "))
        random_numbers.append(num)
    return random_numbers

# Main program
if __name__ == "__main__":
    # Get 5 random numbers from the user
    numbers = get_random_numbers()

    # Display the original list
    print("Original list:", numbers)

    # Sort the list in ascending order
    numbers.sort()

    # Display the sorted list
    print("Sorted list in ascending order:", numbers)
