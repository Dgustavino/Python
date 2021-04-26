import os, sys
import csv

class File_Handler:
    def __init__(self):
        self._data_from_file = self.load_file()

    def load_file(self):
        with open(os.path.join(sys.path[0], "animales.txt")) as file: # loads JSON at same directory level
            data = file.readlines()
        return data

    def write_file(self,valor):
        if valor!=None:
            with open(os.path.join(sys.path[0], "animales.txt"), 'a') as file: 
                file.write("\n"+valor)
            return True
        else:
            return False


test = File_Handler()
print(test.write_file("holahola"))
