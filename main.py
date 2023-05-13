
import random

def play_rock_paper_scissors(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    user_choice = user_choice.lower()

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        if computer_choice == "paper":
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == "paper":
        if computer_choice == "scissors":
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            return "Computer wins!"
        else:
            return "You win!"
    else:
        return "Invalid input. Please choose either 'rock', 'paper', or 'scissors'."

while True:
    user_input = input("Enter your choice \n (rock, paper, or scissors), or 'quit' to exit: ")
    user_input = user_input.strip().lower()
    
    if user_input == "quit":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose either 'rock', 'paper', or 'scissors'.")
        continue
    
    result = play_rock_paper_scissors(user_input)
    print(result)
    print()

print("Thanks for playing!")
