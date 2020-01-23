from playa import *
from utils import *

class Item:
    def __init__(self, oneTime=True, key=False, name=""):
        self.oneTime = oneTime
        self.key = False
        self.msg = ""
        self.name = name
    
    def use(self):
        print("Unusable item. Please report to developer and he'll try to get it fixed :).")
        pass
    
    

class GuildCard(Item):
    def __init__(self):
        super().__init__(False, True, "Guild Card")
        self.msg = "It's a guild card. You can use it to check your status."
    
    def use(self):
        player.dispStats()
    
    def get(self):
        p(self.msg)
        player.inventory.append(self)

class Spellbook(Item):
    def __init__(self):
        super().__init__(False, True, "Spellbook")
    
    def use(self):
        print("Your spells:")
        for i in range(len(player.spells)):
            print("%s.) "%i + player.spells[i].name + " Mana cost: " + str(player.spells[i].mp) + " Damage: " + str(player.spells[i].dmg) + " Accuracy: " + str(round(round(player.spells[i].accur / 256, 3) * 100)) + "%")

