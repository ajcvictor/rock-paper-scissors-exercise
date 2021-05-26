# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# first define the variable of user_choice

user_choice = input("Please choose one of 'rock' , 'paper' , 'scissors': ")

# then print the variable


print("USER CHOICE:" , user_choice)

#validate the input such that it is only one of the expected values
#... will we continue with the rest of the program
#...otherwise we'll stop the program before it tries to do anything else
#...and we'll ask the user to run the program again


#if user_choice = "rock" or "paper" or "scissors:"
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors" ):
    print ("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

# simulate user selection

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice (valid_options)
print ("COMPUTER CHOICE: ", computer_choice)

#determine the winner

if ((user_choice == "rock") and (computer_choice == "scissors")) or ((user_choice == "paper") and (computer_choice == "rock")) or ((user_choice == "scissors") and (computer_choice == "paper")) :
    print ("You won! Thanks for playing. Please play again!")
elif ((user_choice == "rock") and (computer_choice == "rock")) or ((user_choice == "paper") and (computer_choice == "paper")) or ((user_choice == "scissors") and (computer_choice == "scissors")) :
    print ("It's a tie! Thanks for playing. Please play again!")
else:
    print ("Oh, the computer won. It's ok. Thanks for playing. Please play again!")


print("---")  
print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")        