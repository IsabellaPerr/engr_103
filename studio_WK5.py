################################
# Function: health_rating
# Description: Accesses if the given input is dangerous, very unhealthy, unhealthy, unhealthy (for sensitive groups)
# moderate, good. If an error is raised or the number is > 500 or if it is not inside any of the categories then it
# will return invalid
# Parameters: user_input
# Pre-conditions: n/a
# Post-conditions: n/a
###############################

def health_rating(user_input):
    try:
        user_input = float(user_input)

        if 500 < user_input:
            return "invalid"
        if 300 <= user_input:
            return "dangerous"
        if user_input >= 201:
            return "very unhealthy"
        if user_input >= 151:
            return "unhealthy"
        if user_input >= 101:
            return "unhealthy (for sensitive groups)"
        if user_input >= 51:
            return "moderate"
        if user_input >= 0:
            return "good"
    except:
        return "invalid"
    else:
        return "invalid"


user_input = input("Enter the eight hour mean of ozone in micrograms/cubic meter. \n")

print(f"You entered an eight hour mean of {user_input} micrograms/cubic meter\n\
The ozone rating is {health_rating(user_input)}")

# questions:
# should i shadow names from outer scope?
# do i need to put down pre and post conditions
# what happens if i realise my plan should be changed, should i go back and change it or just carry on
# is my try, except statement good?
