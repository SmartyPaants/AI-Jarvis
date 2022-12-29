from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionAnswer
from Body.Listen import MicExecution
print(">> Jarvis is getting ready, wait for a few seconds!")
from Body.Speak import Speak
from Features.Clap import Tester
print(">> Jarvis is ready, clap to start!")

def MainExecution():
    Speak("Hello Sir")
    Speak("How can I assist you sir?")
    while True:
        Data = MicExecution()
        Data = str(Data)
        
        if len(Data) < 3:
            pass

        elif "what is" in Data or "when is" in Data or "where is" in Data or "why is" in Data or "How many" in Data or "how" in Data:
            Reply = QuestionAnswer(Data)
            Speak(Reply)
        
        else:
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