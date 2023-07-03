# Import the random module
import random

# Define the possible characters for the password
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;:,./<>?"

# Define the minimum and maximum password length
min_length = 6
max_length = 255

# Define the ANSI escape sequences for colors
blue = "\033[34m"
green = "\033[32m"
pink = "\033[35m"
reset = "\033[0m"

# Define a function to check if a password is valid
def is_valid(password):
    # Check if the password contains at least one uppercase letter
    if not any(char in uppercase_letters for char in password):
        return False
    # Check if the password contains at least one lowercase letter
    if not any(char in lowercase_letters for char in password):
        return False
    # Check if the password contains at least one number
    if not any(char in numbers for char in password):
        return False
    # Check if the password contains at least one special character
    if not any(char in special_characters for char in password):
        return False
    # If all the checks pass, return True
    return True

# Define a function to color the password according to the character type
def color_password(password):
    # Initialize an empty colored password
    colored_password = ""
    # Loop through each character in the password
    for char in password:
        # Check if the character is a number
        if char in numbers:
            # Add the blue color and the character to the colored password
            colored_password += blue + char
        # Check if the character is a letter
        elif char in uppercase_letters or char in lowercase_letters:
            # Add the green color and the character to the colored password
            colored_password += green + char
        # Check if the character is a special character
        elif char in special_characters:
            # Add the pink color and the character to the colored password
            colored_password += pink + char
    # Add the reset color to the end of the colored password
    colored_password += reset
    # Return the colored password
    return colored_password

# Welcome message
print("Welcome to the Linux User Password Generator!")

# Prompt the user to enter the desired password length and validate it
valid = False
while not valid:
    try:
        length = int(input(f"Please enter the desired password length (between {min_length} and {max_length}): "))
        if min_length <= length <= max_length:
            valid = True
        else:
            print(f"Error: Please enter a number between {min_length} and {max_length}")
    except ValueError:
        print("Error: Please enter a valid number")
    except KeyboardInterrupt:
        print("\nExiting the program...")
        break

# Generate a random password if the length is valid
if valid:
    # Initialize an empty password
    password = ""

    # Loop until the password is valid
    while not is_valid(password):
        # Reset the password to empty string
        password = ""
        # Generate a random password of the desired length
        for i in range(length):
            # Choose a random character from all possible characters
            password += random.choice(uppercase_letters + lowercase_letters + numbers + special_characters)

    # Display the generated password to the user without colors
    print("\nGenerated password:", password)

    # Color the password according to the character type and display it to the user with colors 
    colored_password = color_password(password)
    print("Colored password:", colored_password)
