import random

def rockPaperScissors():
    programSelect = (random.choice(["rock", "paper", "scissors"]))
    playerChoice = input("Rock, paper, scissors? ").lower()

    if programSelect == playerChoice:
        restart = input("Draw, play again? [y or n]").lower()
        playAgain(restart)
    elif (programSelect == "rock" and playerChoice == "scissors") or (programSelect == "scissors" and playerChoice == "paper") or (programSelect == "paper" and playerChoice == "rock"):
        restart = input("You lose! Play again? [y or n]").lower()
        playAgain(restart)
    elif (playerChoice == "rock" and programSelect == "scissors") or (playerChoice == "scissors" and programSelect == "paper") or (playerChoice == "paper" and programSelect == "rock"):
        restart = input("You win! Play again? [y or n]").lower()
        playAgain(restart)
    else:
        restart = input("Computer *facepalms: Play again? [y or n]").lower()
        playAgain(restart)


def playAgain(restart):
    if restart != "y" and restart != "n":
        print("Oy-vey. Let's just play again (--_)")
    elif restart == "n":
        exit()

#main
gameRunning = True
while gameRunning:
    rockPaperScissors()
