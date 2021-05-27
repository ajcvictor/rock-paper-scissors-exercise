# game.py

import random
import os

from dotenv import load_dotenv # see: https://github.com/theskumar/python-dotenv

load_dotenv() 

PLAYER_NAME = os.getenv("PLAYER_NAME", default="Player One") 
SECRET_PASSWORD = os.getenv("SECRET_PASSWORD")


print("-----")
print(f"Welcome to my Rock, Paper, Scissors App '{PLAYER_NAME}'")
print("Rock, Paper, Scissors, Shoot!")
print("-----")

# first define the variable of user_choice

user_choice = input("Please choose one of 'rock' , 'paper' , 'scissors': ")

# then print the variable


print("USER CHOICE:" , user_choice)

#validate the input such that it is only one of the expected values
#... will we continue with the rest of the program
#...otherwise we'll stop the program before it tries to do anything else
#...and we'll ask the user to run the program again

print("-----")
#if user_choice = "rock" or "paper" or "scissors:"
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors" ):
    print ("VALID. Keep going.")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

# simulate user selection

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice (valid_options)
print ("COMPUTER CHOICE: ", computer_choice)

#determine the winner

if ((user_choice == "rock") and (computer_choice == "scissors")) or ((user_choice == "paper") and (computer_choice == "rock")) or ((user_choice == "scissors") and (computer_choice == "paper")) :
    print ("-----")
    print ("Congratulations! You won! ")
elif user_choice == computer_choice :
    print ("-----")
    print ("It's a tie, try again!")
else:
    print ("-----")
    print ("Oh, the computer won. It's ok. Better luck next time!")


print("-----")       
print(f"Thanks for playing, '{PLAYER_NAME}'! This is the end of the game. Please play again!")