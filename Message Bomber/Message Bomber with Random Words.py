# importing the required libraries
import pyautogui, time

# delay to switch windows
time.sleep(5)
#setting count to 5
count = 5
# loop to spam
while count >= 1:
    # fetch and type each word from the file
    pyautogui.write('Random Annoying Spam Words')
    # press enter to send the message
    pyautogui.press('enter')
    # decrementing count
    count = count - 1
