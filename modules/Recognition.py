#!/usr/bin/env python3

# Need change to object oriented

import queue
import sounddevice as sd # Capture l'audio du microphone
from vosk import Model, KaldiRecognizer
import sys
import json

'''This script processes audio input from the microphone and displays the transcribed text.'''
    
# list all audio devices known to your system
print("Display input/output devices")
print(sd.query_devices()) #Affiche la liste de toutes le periphériques audios 
                            # '>' periphérique d'entrer par défaut
                            # '<' peripherique de sortie par defaut

# get the samplerate - this is needed by the Kaldi recognizer
device_info = sd.query_devices(sd.default.device[0], 'input') # Obtenir le perif d'entre par def '[0]'
                                                                # Si [1] on obtion le perf de sortie
samplerate = int(device_info['default_samplerate']) #####

# display the default input device
#Affiche perif d'entré par def
print("===> Initial Default Device Number:{} Description: {}".format(sd.default.device[0], device_info))

# setup queue and callback function
# Met en place ... et ... fonction
q = queue.Queue()

def recordCallback(indata, frames, time, status): # Cette fontion va mettre les donner recolter par le microphopne dans la calss instassier
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))
    
# build the model and recognizer objects.
print("===> Build the model and recognizer objects.  This will take a few minutes.")
model = Model("model") # Objet qui va permettre l'analise de la parole avec comme paramettre l'emplacement du model
recognizer = KaldiRecognizer(model, samplerate) # Objet qui va traduire le vois en text
recognizer.SetWords(False) # Limite la sortie du module de reconnaissance aux seuls morceaux de texte et non à chaque mot

print("===> Begin recording. Press Ctrl+C to stop the recording ")
# Boucle qui va capturer l'audio et le trascrir en text
try:
    with sd.RawInputStream(dtype='int16',
                           channels=1,

                           callback=recordCallback): # On peut aussi specifier 'device='
        while True:
            data = q.get()
            # Passe encore par le format .wav        
            if recognizer.AcceptWaveform(data):
                recognizerResult = recognizer.Result()
                # convert the recognizerResult string into a dictionary  
                resultDict = json.loads(recognizerResult)
                if not resultDict.get("text", "") == "":
                    print(recognizerResult)
                else:
                    print("no input sound")

except KeyboardInterrupt:
    print('===> Finished Recording')
except Exception as e:
    print(str(e))