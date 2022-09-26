import random

player = input("Select Rock, Paper, or Scissor :").lower()
computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Computer selected: ", computer)

if player == "rock" and computer == "paper":
    print("Computer Won")
elif player == "paper" and computer == "scissor":
    print("Computer Won")
elif player == "scissor" and computer == "rock":
    print("Computer Won")
elif player == computer:
    print("Tie")
else:
    print("Wohooo! You Won.")