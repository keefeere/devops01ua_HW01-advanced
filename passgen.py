#!/usr/bin/env python3

##Linux strong password generator by KeeFeeRe(c)2023

# Import the random and string modules
import random
import string

# Define the possible characters for the password using the string module
# https://docs.python.org/3/library/string.html
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
numbers = string.digits
special_characters = string.punctuation

# Define the minimum and maximum password length
min_length = 6
max_length = 255
def_length = 8
min_count = 1
max_count = 1000


# Define the ANSI escape sequences for colors
# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
blue = "\033[34m"
green = "\033[32m"
pink = "\033[35m"
reset = "\033[0m"

# Define a function to check if a password is valid
def is_valid(password):
    # https://stackoverflow.com/questions/39356688/python-2-7-if-not-any-syntax
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

def pass_gen(length):
    # Initialize an empty password
    password = ""

    # Loop until the password is valid
    while not is_valid(password):
        # Reset the password to empty string
        password = ""
        # Generate a random password of the desired length using the string module's join method 
        # https://www.w3schools.com/python/ref_random_choices.asp
        password = "".join(random.choices(uppercase_letters + lowercase_letters + numbers + special_characters, k=length))
    return password

    

# Welcome message
print("Welcome to the Linux User Password Generator by KeeFeeRe!")

# Prompt the user to enter the desired password length and validate it
valid = False
while not valid:
    try:
        length = int(float(input(f"Please enter the desired password length (between {min_length} and {max_length}, default is {def_length}): ").replace(',', '.')))
        if min_length <= length <= max_length:
            valid = True
        else:
            print(f"Error: Please enter a number between {min_length} and {max_length}")
    except ValueError:
        print("Ok, selecting defaul password length (",def_length,")")
        length = def_length
        valid = True
    except KeyboardInterrupt:
        print("\nExiting the program...")
        exit()
        break


 # Prompt the user to choose whether they want to see the colored output or not and validate their choice 
valid = False 
while not valid:
    try: 
        choice = input("Do you want to see the colored output? (Y/N(default)): ").upper()
        if choice in ["Y", "N"]:
            valid = True 
        else: 
            if choice == '':
                choice = "N"
                valid = True 
                break
            else:
                    print("Error: Please enter Y or N")
    except ValueError: 
            print("Error: Please enter Y or N")
    except KeyboardInterrupt: 
            print("\nExiting the program...")
            exit()
            break 


# Asking for the password count and validate it
count = 1
# Checking the password count input and the range
valid = False
while not valid:
    try:
        # Converting the input to an integer or assigning a default value of 1
        count = int(float(input(f"How many passwords do you want to get?  (default is 1 if no value or errorneus value specifed):").replace(',', '.')))
        # Checking the range
        if count < min_count or count > max_count:
            # Printing an error message
            print(f"The password count must be in the range from {min_count} to {max_count}.")
        else:
            # Continuing the password generation, exit loop
            break
    except ValueError:
        count = 1
        break
    except KeyboardInterrupt:
        print("\nExiting the program...")
        exit()
        break

if choice == "Y":
        print(f"Generating {count} coloured password(s):\n")
    # If the user chooses N, display the generated password to the user without colors 
elif choice == "N":
        print(f"Generating {count} password(s):\n")



for i in range(0, count):
    password = pass_gen(length)
    # If the user chooses Y, color the password according to the character type and 
    if choice == "Y":
        colored_password = color_password(password)
        print( colored_password)
    # If the user chooses N, display the generated password to the user without colors 
    elif choice == "N":
        print(password)


#Display password colors explanation
if choice == "Y":
    print("\nExplanation:")
    print(blue + "Blue" + reset + " means number")
    print(green + "Green" + reset + " means letter")
    print(pink + "Pink" + reset + " means special character")