#######################################################################
# Program Filename: final_project.py
# Author: Isabella Perry
# Date: 6/9/2024
# Description: Given a user input that is a string of reasonable length, encrypt it using a symmetric encryption
# algorithm. Then decrypt it using the same algorithm.
# Input: message_input
# Output: encrypted_message_global, decrypted_message_global
#######################################################################

from numpy import random
import string

CHARACTERS = string.printable
characters_list = []

for i in CHARACTERS:
    characters_list.append(i)


#######################################################################
# Function: set_to_value
# Description: converts a set that contains only a single value into the char it contains
# Parameters: my_set
# Return values: i
# Pre-Conditions: my_set must be a set
# Post-Conditions: function is not tested for anything other than a set containing a singular char
#######################################################################
def set_to_value(my_set):
    for i in my_set:
        return i


#######################################################################
# Function: inputs_valid
# Description: checks if the users input is within the given range of 1-100, if not, the program will end. If any and
# all error are raised during this check it will also output an error message and exit the program.
# Parameters: input_var
# Return values: N/A
# Pre-Conditions: Assumes that the user will only use the printable python characters i.e. no characters that are not
# found on a standard American keyboard
# Post-Conditions: Assures that if the program makes it through the inputs_valid that input_var is in a usable format
#######################################################################
def inputs_valid(input_var):
    try:
        if 1 < len(input_var) > 100:
            print("Error, your message is not within the given range (1-100).")
            exit()
    except:
        print("Error, your input is invalid.")
        exit()


#######################################################################
# Function: generate_key
# Description: generates a key in the form of a dictionary in which each char in CHARACTERS is assigned a random
# char in the parameter string_list
# Parameters: string_list
# Return values: my_dict
# Pre-Conditions: assumes that string_list is at least the same size as CHARACTERS
# Post-Conditions: string_list now has len(CHARACTERS) less chars
#######################################################################
def generate_key(string_list):
    global CHARACTERS
    my_dict = {}

    # loops through a string CHARACTERS which contains all printable characters in python. Makes each char in CHARACTERS
    # a key, then randomly assigns a char from string_list and makes it a value. Then removes said char from the pool
    for i in CHARACTERS:
        random_item = random.choice(string_list)
        my_dict[i] = random_item
        string_list.remove(random_item)
    return my_dict


#######################################################################
# Function: encrypt
# Description: uses a key in the form of a dictionary to encrypt the given message
# Parameters: message, key
# Return values: encrypted_message
# Pre-Conditions: Assumes no errors in the key
# Post-Conditions: creates an encrypted message using a key
#######################################################################
def encrypt(message, key):
    encrypted_message = ""
    for i in message:
        encrypted_message += key.get(i)  # gets the value of said key

    return encrypted_message


#######################################################################
# Function: decrypt
# Description: decrypts a message using a key in the forum of a dictionary
# Parameters: message, key
# Return values: decrypted_message
# Pre-Conditions: Assumes no errors in the key
# Post-Conditions: returns a decrypted message, does the opposite of encrypt() does
#######################################################################
def decrypt(message, key):
    decrypted_message = ""

    # loops through the encrypted message, then finds the key that corresponds to the value of i in the message
    # converts that value into a char then adds it to the decrypted message
    for i in message:
        key_value = {j for j in key if key[j] == i}
        key_value = set_to_value(key_value)
        decrypted_message += key_value
    return decrypted_message


# gets inputs
message_input = input("Enter the message to be encrypted\n")
# checks if inputs are valid
inputs_valid(message_input)


# gets a key in the form of a dictionary using characters_list which is a list of all printable characters in python
# prints key for assignment purposes
key_dict = generate_key(characters_list)
print(key_dict)

# encrypts and prints the message using said dictionary
encrypted_message_global = encrypt(message_input, key_dict)
print(encrypted_message_global)

# prints and decrypts the message using the key_dict
decrypted_message_global = decrypt(encrypted_message_global, key_dict)
print(decrypted_message_global)
