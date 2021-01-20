#importing the required modules
from datetime import datetime   
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS AM/PM\n")
#obtaining the hour, minute, second and period of the alarm time
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11]

print("Alarm Set!")

while True:
#obtaining the current time
    now = datetime.now()
#obtaining the hour, minute, second and period of the current time
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period and alarm_hour==current_hour and alarm_minute==current_minute and alarm_seconds==current_seconds):
        print("Wake Up!")
        playsound('/path/to/a/sound/file/you/want/to/play.mp3')
        break
