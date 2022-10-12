import os

class Play():
    def __init__(self,pathdirectory,sysPlayer):
        self.pathdirectory = pathdirectory
        self.sysPlayer = sysPlayer


    def playMedias(self):
        for song in os.listdir(path=self.pathdirectory):#all files in path
            os.system(f'{self.pathdirectory}\{song}')
            
# At the moment this focntion is not worked 
    def stop(self):
        os.system(f'taskkill /f /im {self.sysPlayer}')
