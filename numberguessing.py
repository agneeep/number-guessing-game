####
# Number Guessing Game
###

import random
computer_choice=random.randint(1,100)

while True:
    try:
        user_choice=input("Pick a number between 1 and 100: ")
        if int(user_choice)>=1 and int(user_choice)<=100:
            if int(user_choice) != computer_choice:
                if int(user_choice) > computer_choice:
                    print("Too high! Try again.")
                elif int(user_choice) < computer_choice:
                    print("Too low! Try again.")
            elif int(user_choice) == computer_choice:
                print("That's right! The secret number was", computer_choice)
                break
    except:
        print(user_choice, "is not a valid number.")