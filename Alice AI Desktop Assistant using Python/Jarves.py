from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print('>> Starting the Alice : Wait for some seconds.');
from Body.speak import Speak
from Features.Clap import Tester
print('>> Starting the Alice : please clap wakeup the Alice.');



def MainExe():

    Speak("Hello Sir")
    Speak("I am Alice, I am Ready To Assist You Sir.")

    while True:
        data = MicExecution()
        data = str(data)
        Reply = ReplyBrain(data)
        Speak(Reply)
        
def clapDetect():
    querys = Tester()
    if "True-Mic" in querys:
        print('')
        MainExe()
    else:
        pass

clapDetect()