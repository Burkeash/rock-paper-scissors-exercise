
import random

import os

import dotenv

dotenv.load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME")
print(PLAYER_NAME)


print("Welcome", PLAYER_NAME, "Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'papers', 'scissors': ")

#print(user_choice)
print("USER CHOICE:", user_choice)

#validate the input such that only if it is one of the expected values


if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE:", computer_choice)


#determining who won:

if (user_choice == "rock") and (computer_choice == "scissors"):
   print("You won!")
if (user_choice == "scissors") and (computer_choice == "paper"):
    print("You won!")
if (user_choice == "paper") and (computer_choice == "rock"):
    print("You won!")
if (user_choice == "rock") and (computer_choice == "paper"):
    print("You lost!")
if (user_choice == "scissors") and (computer_choice == "rock"):
    print("You lost!")
if (user_choice == "paper") and (computer_choice == "scissors"):
    print("You lost!")
if (user_choice == computer_choice):
    print("You tied!")

# configure player name via env variables

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN")