# Rock Paper Scissor
from random import randint

# Moves for the player
moves = ["rock", "paper", "scissor"]

while True:
    # computer chooses random
    computer = moves[randint(0, 2)]
    player = input("Rock, Paper, Scissors? {or end the game} :").lower()
    if player == "end the game" or player == "end":
        print("The Game has ended.")
        break
    # if computer chooses same as player
    elif player == computer:
        print("Tie")
    # if player chooses rock
    elif player == "rock":
        if computer == "paper":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win", player, "beats", computer)
    # if player chooses paper
    elif player == "paper":
        if computer == "scissor":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win", player, "beats", computer)
    # if player chooses scissors
    elif player == "scissor":
        if computer == "rock":
            print("You Lose!", computer, "beats", player)
        else:
            print("You Win", player, "beats", computer)
    # if there is a spelling mistake
    else:
        print("Check your spelling......")
