from utils import *

class Location:
    def __init__(self, x, y, major_locs, minor_locs=[]):
        self.x = x
        self.y = y
        self.majorB = major_locs
        self.minorB = minor_locs
    
    def look(self):
        while 1:
            while 1:
                print("1. Look for major buildings")
                print("2. Look for everything")
                try:
                    inp = int(input(">"))
                    break
                except:
                    p("Please enter a number.")
                    continue
            if inp == 1:
                while 1:
                    for i in self.majorB:
                        p(str(self.majorB.index(i) + 1) + ".) " + i.name)
                    try:
                        inp2 = int(input(">"))
                        break
                    except:
                        p("please enter a number.")
                self.majorB[inp2 - 1].enter()

                
            if inp == 2:
                for i in range(len(self.majorB) - 1):
                    p("%s.) "%i + self.majorB[i].name)
                for j in range(len(self.minorB) - 1):
                    p("%s.) "%(j + len(self.majorB - 1)) + self.minorB[i].name)

    def enter(self):
        #Do some entrance dialogue
        self.look()
