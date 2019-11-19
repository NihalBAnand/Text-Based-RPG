from utils import *
from items import *
import main
import imp

class Person:
    def __init__(self, name="Error", hasItem=False, hasQuest=False, item=None):
        self.hasItem = hasItem
        self.hasQuest = hasQuest
        self.item = item
        self.name = name
    
    def quest(self):
        #Put give quest text here
        pass

    def item(self):
        #Put give item text here
        pass

    def talk(self):
        p("Hello, my name is %s. This is filler text because some dumb schmuck forgot to write dialogue for me."%self.name)

class ReceptionistKate(Person):
    def __init__(self):
        super().__init__("Receptionist Kate", True, False, GuildCard())
    
    def talk(self):
        imp.reload(main)
        p("%s: Hello, and welcome to the Falaria branch of the Adventurer's Guild. How can I help you today?" %self.name)
        p(main.player.name + ": Yes, I'd like to register as an adventurer.")
        p(main.player.name)
        p("%s: Alrighty then, give me a moment." %self.name)
        p("...", 0.75, 0.75)

    def item(self):
        imp.reload(main)
        p("%s: Here you are!"%self.name)
        self.item.get()
        p("Press enter to continue")
        input("")
    