from utils import *
from items import *
from playa import *

class Person:
    def __init__(self, name="Error", hasItem=False, hasQuest=False, item=None):
        self.hasItem = hasItem
        self.hasQuest = hasQuest
        self.item = item
        self.name = name
    
    def quest(self):
        #Put give quest text here
        pass

    def giveItem(self):
        #Put give item text here
        pass

    def talk(self):
        p("Hello, my name is %s. This is filler text because some dumb schmuck forgot to write dialogue for me."%self.name)

class ReceptionistKate(Person):
    def __init__(self):
        super().__init__("Receptionist Kate", True, False, GuildCard())
    
    def talk(self):
        p("%s: Hello, and welcome to the Falaria branch of the Adventurer's Guild. How can I help you today?" %self.name)
        p("%s: Yes, I'd like to register as an adventurer."%player.name)
        p("%s: Alrighty then, give me a moment." %self.name)
        p("...", 0.75, 0.75)
        self.giveItem()

    def giveItem(self):
        p("%s: Here you are!"%self.name)
        self.item.get()
        p("Press enter to continue")
        input("")
    