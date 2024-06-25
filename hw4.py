#######################################################################
# Program Filename: hw4.py
# Author: Isabella Perry
# Date: 5/15/2024
# Description: Calculates and displays the amount of radioactive decay of aluminium during both activation and decay
# at intervals of 30 seconds
# Input: mass of aluminium, time steps
# Output: decay per second at 30 second time intervals and final decay per second during both activation and decay
#######################################################################

import math

# defining constants
DECAY_CONST = 0.005145  # lambda
AV = 6.022 * (10 ** 23)  # avogadro's number
NEUTRON_FLUX = 10 ** 8  # phi
CROSS_SECTION = 231 * (10 ** -24)  # sigma
MW = 26.981539  # molecular weight of al (aluminium)


#######################################################################
# Function: activation
# Description: returns the amount of decay per second for the given time
# Parameters: time, mass
# Return values: amount of decay per second
# Pre-Conditions: N/A
# Post-Conditions: returns the amount of decay per second
#######################################################################
def activation(time, mass):
    global DECAY_CONST, AV, NEUTRON_FLUX, CROSS_SECTION, MW
    return NEUTRON_FLUX * CROSS_SECTION * (mass * AV / MW) * (1 - math.exp(-1 * DECAY_CONST * time))


#######################################################################
# Function: decay
# Description: calculates amount of decay per second after the activation period
# Parameters: activation_decay_final
# Return values: decay per second during decay period
# Pre-Conditions: none
# Post-Conditions: none
#######################################################################
def decay(activation_decay_final, time):
    global DECAY_CONST
    return activation_decay_final * math.exp(-1 * DECAY_CONST * time)


######################################################################
# Function: input_valid
# Description: check to see if the users input is in a valid format i.e. must be a float or an int, must be a
# positive number
# Parameters: user_input
# Return values: void
# Pre-Conditions: none
# Post-Conditions:
#######################################################################
def input_valid(user_input):
    is_int = isinstance(user_input, int)
    is_float = isinstance(user_input, float)

    if not (is_int or is_float):
        print("Error, your number must be an int or float.")
        exit()

    # question should 0 be a valid input
    if user_input < 0:
        print("Error, your input is not positive")
        exit()


# getting inputs
al_mass = float(input("What is the mass of al in grams? (0.000001-1)\n"))  # 10^-6 < m < 1

# amount of time for the activation period
time_steps = int(input("What is the number of time steps? (60-600)\n"))  # time of activation period

# checking if inputs are valid
input_valid(al_mass)
input_valid(time_steps)

if not ((10 ** -6) <= al_mass <= 1):
    print("The given mass is not within the given range")
    exit()

if not (60 <= time_steps <= 600):
    print("The given time steps is not within the given range")
    exit()
# end of checking

# activation loop, starts at 30 seconds ends at time_steps and increments by 30. Prints out the activation decay
# every 30 seconds of activation or every 1 iteration
for i in range(30, time_steps + 1, 30):
    print(f"At time step {i} the activity is {activation(i, al_mass)} dps")

final_activity = activation(time_steps, al_mass)

print(f"The final activity from activation is {final_activity} dps")
print("STARTING DECAY")

current_activity = final_activity
time_sense_activation = 30

# Prints the decay values during the decay period until the rate of decay is 25% of its original value,
# increments 30 seconds
while (current_activity / final_activity) > 0.25:
    current_activity = decay(final_activity, time_sense_activation)
    print(f"At time step {time_sense_activation} the activity is {current_activity} dps")

    time_sense_activation += 30
