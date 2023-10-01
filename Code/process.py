import speech_recognition
import pyttsx3
from datetime import date, datetime


robot_ear = speech_recognition.Recognizer()
engine = pyttsx3.init()
robot_brain =""

with speech_recognition.Microphone() as mic:
    print("Jessica : I'm listening")  
    audio = robot_ear.listen(mic)
    
print("Jessica:...")
try:    
    you = robot_ear.recognize_google(audio)
    print("You:" + you)
except:
    you = ""
    
if you == "": 
    robot_brain = "I can't hear you, try again"
elif you == "hello":
    robot_brain = "Hello Tung Anh"
elif you == "what's the weather today":
    robot_brain= "it's rain today"
elif you == "what's your name":
    robot_brain = "My name is jessica"
elif you == "today":
    today = date.today()
    robot_brain = today.strftime("%B %d, %Y")
elif you == "time":
    now = datetime.now()
    robot_brain = now.strftime("%H hours %M minutes %S seconds")
else:
    robot_brain = "I can't understand"
    
print("Jessica:" + robot_brain)



voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[1].id)
engine.say(robot_brain)
engine.runAndWait()