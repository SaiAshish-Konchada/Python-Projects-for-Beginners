# importing the required libraries
import pyautogui, time

# delay to switch windows
time.sleep(10)
# content you want to spam with
f = open("idoc.pub_green-lantern-movie-script.txt", 'r')
# loop to spam
for word in f:
    # fetch and type each word from the file
    pyautogui.write(word)
    # press enter to send the message
    pyautogui.press('enter')
