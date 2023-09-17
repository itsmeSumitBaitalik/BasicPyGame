import pyttsx3
import time

t = time.strftime('%H:%M:%S')
curr_time = time.strftime('%H hour %M minutes %S second')
engine = pyttsx3.init()
engine.say("current time is:"+curr_time)
engine.runAndWait()
if (curr_time>str(0) and curr_time<str(12)):
    engine.say("Good morning")
    engine.runAndWait(1)
elif (curr_time>str(12) and curr_time<str(16)):
    engine.say("Good afternoon")
    engine.runAndWait()
elif (curr_time>str(12) and curr_time<str(20)):
    engine.say("Good evening")
    engine.runAndWait()
else:
    engine.say("Good night")
    engine.runAndWait()