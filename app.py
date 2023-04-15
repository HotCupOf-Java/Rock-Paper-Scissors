#Firstly create a basic, one run version of the game
#introduce the while loop and break requirements
#Create exception handling

import random
import time




print("Welcome to Rock, Paper, Scissors.\n")
input("Press Enter to start.")


while True:

    win=0
    lose=0
   
    print("Type either 'Rock', 'Paper', or 'Scissors' to make your choice\n")
    player_choice  = input("Enter your choice: ").lower()

    while player_choice not in ["rock","paper","scissors"]:
        player_choice=input("Please enter a valid option: ").lower
    else:
        print("Now the computer decides...")
    
    time(0.5)
    
    def computer_choice():
        computer = random.randint(0,2)
        if computer == 0:
            computer_choice = "rock"
        elif computer == 1:
            computer_choice = "paper"
        else:
            computer_choice = "scissors"
        return computer_choice


    computer_choice= computer_choice()
    print(computer_choice)

#This is the decision tree to compare choices
    def rock_paper_scissors(player_choice, computer_choice):
        if player_choice == "rock":
            if computer_choice == "rock":
                print("It's a draw!")
            elif computer_choice == "paper":
                print("You lose!")
                lose +=1
            elif computer_choice == "scissors":
                print("You win!")
                win +=1
        elif player_choice == "paper":
            if computer_choice == "rock":
                print("You win!")
                win +=1
            elif computer_choice == "paper":
                print("It's a draw!")
            elif computer_choice == "scissors":
                print("You lose!")
                lose +=1
        elif player_choice == "scissors":
            if computer_choice == "rock":
                print("You lose!")
                lose +=1
            elif computer_choice == "paper":
                print("You win!")
                win +=1
            elif computer_choice == "scissors":
                print("It's a draw!")
    time(1)

    rock_paper_scissors(player_choice,computer_choice)

    print()    
    print(f"Wins: {win}")
    print(f"Loses: {lose}")
    

    if win > lose:
        print("You're winning!\n")
    elif win < lose:
        print("Uh oh, you're losing!\n")
    else:
        print("You're tied!\n")

    play_again=input("Do you want to play again? [y,n]: ").lower

    while play_again not in ["y", "n"]:
        play_again=input("Please enter a valid choice: ").lower

    if play_again == "n":
        break


    