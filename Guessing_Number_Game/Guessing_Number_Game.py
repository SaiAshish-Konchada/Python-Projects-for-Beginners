import random

n = random.randrange(1, 10)
guess = int(input("Guess any number between 1-10: "))
while n != guess:
    if guess < n:
        print("Too low")
        guess = int(input("Try again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Try again: "))

print("Wohoo! You guessed it right.")
