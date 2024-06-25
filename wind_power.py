import math


#####################################################
# Program FileName: wind_power.py
# Author: Isabella Perry
# Date: 4/22/2024
# Description: A program which calculates the maximum and actual power output of a wind turbine
# Input: wind speed [m/s], blade radius [m], operating efficiency [%]
# Output: max power and actual power
##########################################################


##########################################################
# Function: data_cleaning
# Description: makes sure that the argument is positive, is less than 10000 and is larger than 0.001,
# and is either a float or an int. If any of those conditions are not met it will give an error message and exit the
# program
# Parameters: user_input
# return values: none
# Pre-Conditions: No expectations of arguments
# Post-Conditions: No output or return values
#####################################################

def data_cleaning(user_input):
    is_float = isinstance(user_input, float)
    is_int = isinstance(user_input, int)

    if user_input < 0:
        print("Error, your number cannot be negative")
        exit()

    if not (is_float or is_int):
        print("Error, your number must be a float or int.")
        exit()

    if (user_input > 10000) or (user_input < 0.001):
        print("Error, input is too large or small.")
        exit()


# Defining constants

PI = 3.1415
AIR_DENSITY = 1.2

# Gathering inputs and converting the data type to a float

wind_speed = float(input("Enter the wind speed: \n"))
blade_radius = float(input("Enter the blade radius: \n"))
operating_efficiency = float(input("Enter operating efficiency: \n"))

# Cleaning all three variables which were declared above
data_cleaning(wind_speed)
data_cleaning(blade_radius)
data_cleaning(operating_efficiency)

# Converting the operating efficiency from a percentage to a decimal
operating_efficiency /= 100

# Using the formula of a circle where the blade radius is the radius of the cross-section
blade_area = PI * math.pow(blade_radius, 2)

# Using the formula for the power out put of a wind turbine and deciding the result by 1000 to convert watt-hours
# to kilowatt-hours

max_power = (blade_area * 0.5 * AIR_DENSITY * math.pow(wind_speed, 3)) / 1000

# Converting the max power to actual power by multiplying it by the operating efficiency
actual_power = max_power * operating_efficiency

# Out putting the data for the user
print(f"The max power of the wind turbine is {max_power} kWh. The actual power is {actual_power} kWh.")
