# This module work to modifie file name for the Play module
import os

class Files():
    def __init__(self, pathdirectory, toReplace, replaceBy):
        self.pathDirectory = pathdirectory
        self.toReplace = toReplace
        self.replaceBy = replaceBy

    def renameFiles(self):
        for data in os.listdir(path=self.pathDirectory):
            newFile = data.replace(self.toReplace, self.replaceBy)
            os.rename(f"{self.pathDirectory}\{data}", f"{self.pathDirectory}\{newFile}")


