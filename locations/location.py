from utils import *
from playa import *
import playa

class Location:
    def __init__(self, x, y, major_locs):
        self.x = x
        self.y = y
        self.majorB = major_locs
        playa.player.locations.append(self)
        self.playerEntered = False
    
    def look(self):
        while 1:
            while 1:
                print("1. Look around")
                print("2. Display Inventory")
                print("3. Leave town")
                try:
                    inp = int(input(">"))
                    break
                except:
                    p("Please enter a number.")
                    continue
            if inp == 1:
                while 1:
                    m = 1
                    for i in self.majorB:
                        print(str(self.majorB.index(i) + 1) + ".) " + i.name)
                        m += 1
                    print(str(m) + ".) Exit")
                    
                    try:
                        inp2 = int(input(">"))
                        self.majorB[inp2 - 1].enter()
                        break
                    except:
                        if inp2 == m:
                            break
                        else:
                            print("Please enter a valid number.")
                

            if inp == 2:
                playa.player.dispInv()
            
            if inp == 3:
                self.exit()

    def enter(self):
        #Do some entrance dialogue
        self.look()
        self.playerEntered = True

    def exit(self):
        playa.player.OVx -= 1
        playa.player.overworld()
