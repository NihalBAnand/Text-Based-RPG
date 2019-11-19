from utils import *

class Player:
    def __init__(self):
        self.race = None
        self.job = None
        self.name = "Feff"

        self.OVx = 0
        self.OVy = 0
        self.Dx = 0
        self.Dy = 0
        self.inDungeon = False

        self.hp = 100
        self.maxhp = 100
        self.sp = 100
        self.maxsp = 100
        self.mp = 100
        self.maxmp = 100

        self.exp = 0
        self.lvl = 1
        self.exp2lvl = 50

        self.affinityBonus = 5

        self.strength = 1
        self.magic = 1
        self.speed = 10
        self.defense = 1

        self.stats = [self.maxhp, self.maxmp, self.maxsp, self.strength, self.magic, self.speed, self.defense]
        self.affinities = []

        self.tempDefense = 0

        self.armor = None

        self.weapons = []
        self.spells = []
        self.inventory = []
    
    def attack(self, enemy, weapon):
        hasAffin = weapon in self.affinities
        enemy.hp -= weapon.dmg * ((round(strength / 2)) + 1 + (hasAffin*self.affinityBonus))
    
    def move(self):
        while 1:
            print("1. North")
            print("2. South")
            print("3. East")
            print("4. West")
            try:
                inp = int(input(">"))
                break
            except:
                p("Please type a number.")
                continue
        if self.inDungeon:
            if   inp == 1: self.Dy += 1
            elif inp == 2: self.Dy -= 1
            elif inp == 3: self.Dx += 1
            elif inp == 4: self.Dx -= 1
        else:
            if   inp == 1: self.OVy += 1
            elif inp == 2: self.OVy -= 1
            elif inp == 3: self.OVx += 1
            elif inp == 4: self.OVx -= 1
    
    def levelUp(self):
        p("Congratulations! You've leveled up! Pick a bonus.")
        while 1:
            print("1. Max health + 10")
            print("2. Mana pool + 10")
            print("3. Full stamina + 10")
            print("4. Strength + 5")
            print("5. Magic Power + 5")
            print("6. Agility + 3")
            print("7. Defense + 3")
            try:
                inp = int(input(">"))
                break
            except:
                p("Please input a number.")
        if inp == 1:
            self.maxhp += 10
        elif inp == 2:
            self.maxmp += 10
        elif inp == 3:
            self.maxsp += 10
        elif inp == 4:
            self.strength += 5
        elif inp == 5:
            self.magic += 5
        elif inp == 6:
            self.speed += 3
        elif inp == 7:
            self.defense += 3
        self.race.bonus += self.race.levelUp()
    
    def dispStats(self):
        #Leveling
        print("Level: %s" %self.lvl)
        print("EXP: %s" %self.exp)
        print("EXP to level up: %s" %self.exp2lvl)

        #Point-based stats
        print("Max Health: %s" %self.maxhp)
        print("Current Health: %s" %self.hp)
        print("Mana Pool: %s" %self.maxmp)
        print("Current Mana: %s" %self.mp)
        print("Stamina Pool: %s" %self.maxsp)
        print("Current Stamina: %s" %self.sp)

        #Battle Stats
        print("Strength: %s" %self.strength)
        print("Magic Power: %s" %self.magic)
        print("Agiity: %s" %self.speed)
        print("Defense: %s" %self.defense)
        

