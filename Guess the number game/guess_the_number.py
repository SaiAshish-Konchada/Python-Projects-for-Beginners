import random
number = random.randint(1,10)
for i in range(0,3):
    user = int(input("Guess the lucky number"))
    if user == number:
        print("Hurray!!")
        print(f"You guessed the number right, it's {number}")
        break
if user != number:
    print(f"Your guess is incorrect the number  is {number}")
