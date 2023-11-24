import os
import gui

class printerC:
    def __init__(self):
        pass
    def printOut(self, count):
        os.startfile("Images\\img{}.png".format(count), 'print')
