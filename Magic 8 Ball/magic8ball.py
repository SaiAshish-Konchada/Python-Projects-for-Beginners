# importing the required libraries
import random
import pyfiglet
import time

# defining function magic8ball()
def magic8ball():
    # print aesthetic text design
    print(pyfiglet.figlet_format("Magic 8 Ball"))
    # asking for player's name
    name = input('Hey there, I am the Magic 8 Ball, What is your name? ')
    # greeting the player
    print('Hello ' + name + '!')
    # calling the magic_questions() function to ask for question and give magic response
    magic_questions()

# defining the function magic_questions()
def  magic_questions():
    # list of answers the ball replies
    answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it",
               "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
    input('Ask me a question ')
    # simulating the thinking process
    print("Thinking...")
    time.sleep(1)
    print("Gathering possible answer...")
    time.sleep(2)
    # printing out a random answer from the list of possible answers
    print(answers[random.randint(0, len(answers)-1)] )
    time.sleep(3)
    # calling the Replay to check if the player wants to play again
    Replay()

# defining the Replay function()
def Replay():
    # asking the player's interest in playing again
    print('Do you have another question? [Yes/No] ')
    # converting the response to lower case to avoid capitalisation issues
    reply = input().lower()
    # if yes, resume the game again from the question-answer part
    if reply == 'yes':
        magic_questions()
    # if no, stop the execution of the program
    elif reply == 'no':
        exit()
    # in case of an invalid response, ask the player to enter a valid choice
    else:
        print('Apologies, Please enter Yes or No')
        Replay()

# calling the magic8ball() function to recursively activate the other functions too
magic8ball()
