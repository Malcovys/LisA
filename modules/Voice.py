
import pyttsx3

class Voice():

    def __init__(self):    
        self.engine = pyttsx3.init()
        self.voice = self.engine.getProperty('voices')
        
    def voiceParameter(self,language):
        self.engine.setProperty('voice', language)
    
    def toSpeak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
