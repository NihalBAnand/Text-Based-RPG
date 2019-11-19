from locations.buildings.building import Building
from person import *
from items import *
from utils import *

class Guild(Building):
    def __init__(self):
        super().__init__(True)
        self.guildCard = GuildCard()
        self.receptionist = ReceptionistKate()
        self.name = "Adventurer's Guild"
    
    def enter(self):
        p("You enter the guild hall.")
        p("The place is a cacophony of laughter, jovial shouting, and klinks of glasses and dishes.\nOverwhelmed wait staff weave their way through the tumult, taking orders, carrying dishes, serving food and drink, and sometimes giving a quip or two, usually met with more laughter.")
        p("All different kinds of people gather here, of different races, jobs, and social classes.")
        p("Across the room from you, you can vaguely make out a receptionist waving you over.")
        p("You make your way over, wading through the sea of people.")
        self.receptionist.talk()

