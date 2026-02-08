#RPS.py
#Name:Gavin Grow
#Date:2/8/26
#Assignment:RPS
import random

def main():
    wins = 0
    ties = 0
    losses = 0

    playing = True
## computer picks while user picks
    while playing:
        player = input("Choose your fighter! R, P, or S: ").upper()
        computer = random.choice(['R', 'P', 'S'])
## after they both pick , code will go through elif statements till finds one.
        if computer == "R":
            print("Computer chooses Rock")
        elif computer == "P":
            print("Computer chooses Paper")
        else:
            print("Computer chooses Scissors")

        if computer == player:
            print("You tied!")
            ties += 1
        elif (player == "R" and computer == "S") or \
             (player == "P" and computer == "R") or \
             (player == "S" and computer == "P"):
            print("You beat the computer!")
            wins += 1
        else:
            print("Computer beat you!")
            losses += 1

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            playing = False
##if they are done print this
    print("\nFinal Stats")
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties, "\t", losses)


if __name__ == '__main__':
    main()
