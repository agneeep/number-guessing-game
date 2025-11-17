####
# Number Guessing Game
###

import random

best_score=None

while True:
    while True:
        try:
            min_value=int(input("Pick the minimum value for your range: "))
            max_value=int(input("Pick the maximum value for your range: "))
            if min_value>max_value:
                print("The minimum value cannot be higher than the maximum.")
                continue
            break
        except ValueError as string_e:
            print("Strings are not valid values.")

    computer_choice=random.randint(min_value, max_value)

    max_attempts=5

    for attempt in range(1,6):
        try:
            user_choice=input("Pick a number between " + str(min_value) + " and " + str(max_value) + ": ")
            if int(user_choice)>=min_value and int(user_choice)<=max_value:
            
                if int(user_choice) != computer_choice:
                    if attempt==max_attempts:
                        print("Game over!")
                        print("The secret number was ", computer_choice)
                        break
                    elif int(user_choice) > computer_choice:
                        print("Too high! Try again.")
                    elif int(user_choice) < computer_choice:
                        print("Too low! Try again.")
                
                elif int(user_choice) == computer_choice:
                    print("That's right! The secret number was", computer_choice)
                    if best_score is None or attempt < best_score:
                        best_score = attempt
                        print("That's a new best score!")
                    break
            
            elif int(user_choice)<min_value or int(user_choice)>max_value:
                print("Your selected value is not within the range.")
        except ValueError as string_e:
            print(user_choice, "is not a valid number.")

    print("Best score: ", best_score)

    
    while True:
        play_again=input("Would you like to play again? (y/n) ").lower()
        if play_again=="y":
            continue
        elif play_again=="n":
            break
        else:
            print(play_again, " is not a valid response.")
            continue
    
    if play_again=="n":
        break
        
