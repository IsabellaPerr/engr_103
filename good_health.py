#####################################################
# Program FileName: good_health.py
# Author: Isabella Perry
# Date: 5/05/2024
# Description: Given an input of the users SP and DP, calculate the users PP and MAP
# Output: PP, MAP, and their respective too high/low values
##########################################################

##########################################################
# Function: data_cleaning
# Description: makes sure that the argument is positive and is either a float or an int.
# If any of those conditions are not met it will give an error message and exit the
# program
# Parameters: user_input
# return values: none
# Pre-Conditions: No expectations of arguments
# Post-Conditions: No output or return values
#####################################################
def data_cleaning(user_input):
    is_int = isinstance(user_input, int)
    is_float = isinstance(user_input, float)

    if user_input < 0:
        print("Error, your number cannot be negative")
        exit()

    if not (is_int or is_float):
        print("Error, your number must be an int.")
        exit()

    if (user_input > 10000) or (user_input < 0.001):
        print("Error, input is too large or small.")
        exit()

##########################################################
# Function: calc_pp
# Description: subtracts argument 1 from argument 2
# Parameters: sp, dp
# return values: sp - dp
# Pre-Conditions: No expectations of arguments
# Post-Conditions: No output or return values
#####################################################


def calc_pp(sp, dp):
    return sp - dp


##########################################################
# Function: calc_map
# Description: calculates mean arterial pressure
# Parameters: dp, pp
# return values: dp + (1/3) * pp
# Pre-Conditions: No expectations of arguments
# Post-Conditions: returns a float
#####################################################
def calc_map(dp, pp):
    return dp + (1 / 3) * pp


##########################################################
# Function: map_high_low_normal
# Description: calculates whether the users MAP is too high/low or normal
# Parameters: map_input
# return values: normal or too low
# Pre-Conditions: argument must be int or float
# Post-Conditions: returns a string
#####################################################
def map_high_low_normal(map_input):
    if map_input > 60:
        return "normal"
    return "too low"


##########################################################
# Function: pp_high_low_normal
# Description: calculates whether the users PP is too high/low or normal
# Parameters: pp_input
# return values: normal or too high
# Pre-Conditions: argument must be int or float
# Post-Conditions: returns a string
#####################################################


def pp_high_low_normal(pp_input):
    if pp_input > 80:
        return "too high"
    return "normal"


# getting inputs
SP = float(input("Enter the users SP\n"))
DP = float(input("Enter the users DP\n"))

# cleaning data
data_cleaning(SP)
data_cleaning(DP)

# makes sure SP is greater to or equal to DP, by definition this should be false if the inputs are correct
if SP <= DP:
    print("SP smaller or equal to DP")
    exit()

# calculating PP and MAP
PP = calc_pp(SP, DP)
MAP = calc_map(DP, PP)

# getting the high low normal values of MAP and PP
map_value = map_high_low_normal(MAP)
PP_value = pp_high_low_normal(PP)

print(f"The users PP is {PP} which is {PP_value} mmHG. The users MAP is {MAP} mmHG which is {map_value}")
