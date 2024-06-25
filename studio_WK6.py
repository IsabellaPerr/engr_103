import random

guess_number = 0
answer = random.randint(1, 10)
guess = 0


def get_guess():
    return int(input("Enter your guess\n"))


def answer_correct(given_input):
    return given_input == answer


while guess_number < 5:
    guess = get_guess()

    if answer_correct(guess):
        print("Correct")
        exit()

    print("incorrect")
    guess_number += 1

print(f"The correct answer is {answer}")
