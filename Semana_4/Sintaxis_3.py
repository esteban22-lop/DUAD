#Sintaxis 3

import random

random_number = random.randint(1, 10)
guess = 0

while guess != random_number:
    guess = int(input("Guess the number I'm thinking between 1 to 10: "))
    
    if guess < random_number:
        print("Sorry, but is greater than this one.")
    elif guess > random_number:
        print("Almost there, but smaller.")
    else:
        print("You got it!")