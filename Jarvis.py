from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting Jarvis, Wait for a few seconds!")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Starting Jarvis, Wait for a some seconds!")

def MainExecution():
    Speak("Hello Sir")
    Speak("How can I assist you sir?")
    while True:
        Data = MicExecution()
        Data = str(Data)
        Reply = ReplyBrain(Data)
        Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("") 
        print(">> Clap Detected!! Starting Jarvis")
        print("")
        MainExecution()
    else:
        pass

ClapDetect()