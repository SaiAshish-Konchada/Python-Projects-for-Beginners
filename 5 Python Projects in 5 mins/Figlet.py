import os
from pyfiglet import Figlet

def cool(text):
    cooltext  = Figlet(font="slant")
    os.system("cls")
    return str(cooltext.renderText(text))

if __name__ == '__main__':
    print(cool("Sai Ashish"))
