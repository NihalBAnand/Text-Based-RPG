import utils
import random
from enemies import *

class Player:
    def __init__(self):

        self.race = None
        self.job = None
        self.name = "Feff"

        self.OVx = 5
        self.OVy = 5
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

        self.locations = []

        self.tempDefense = 0

        self.armor = None

        self.weapons = []
        self.spells = []
        self.inventory = []
    
    def attack(self, enemy, weapon, strong=1):

        hasAffin = weapon in self.affinities
        dmg = round((weapon.dmg * ((round(self.strength / 2)) + 1 + (hasAffin*self.affinityBonus)) * strong) * random.uniform(.5, 1.5))
        enemy.hp -= dmg

        utils.p("You strike your foe for " + str(dmg) + " damage.")
    
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
                utils.p("Please type a number.")
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
        for loc in self.locations:
            if self.OVx == loc.x and self.OVy == loc.y:
                loc.enter()
    
    def levelUp(self):
        utils.p("Congratulations! You've leveled up! Pick a bonus.")
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
                utils.p("Please input a number.")
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
    
    def dispInv(self):
        while 1:
            for i in range(0, len(self.inventory)):
                print(("%s.) " % str(i + 1)) + self.inventory[i].name)
            utils.p("What would you like to use? Type 'exit' to quit.")
            inp = input(">")

            try:
                inp = int(inp)
            except:
                if inp.lower() == "exit": break

            try:
                self.inventory[inp - 1].use()
                break
            except:
                utils.p("Please type a valid number.")
            

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
    
    def randomEnc(self, lookedF = False, resting = False):
        chance = random.randint(0, 100)
        if lookedF:
            if chance > 25:
                self.battle(Zombie())
            else:
                print("You didn't find anything to fight.")
        elif resting:
            if chance > 45:
                utils.p("You are abushed while you rest!")
                self.battle(Zombie())
        else:
            if chance > 60:
                self.battle(Zombie())
            else:
                pass
    
    def overworld(self):
        while 1:
            print("X: " + str(self.OVx))
            print("Y: " + str(self.OVy))
            print("1.) Move")
            print("2.) Open Inventory")
            print("3.) Look for trouble")
            print("4.) Rest for the day")
            try:
                inp = int(input(">"))
                if inp == 1: self.move()
                elif inp == 2: self.dispInv()
                elif inp == 3: self.randomEnc(True)
                elif inp == 4: self.rest()
                else: utils.p("Please enter a number displayed, dummy.")
            except:
                utils.p("Please enter a number.")
    
    def rest(self):
        utils.p("You set up camp for the day.")
        self.randomEnc(resting = True)
        utils.p("...", .75, .5)
        utils.p("You feel ready for your adventure ahead!")
        self.hp = self.maxhp
        self.sp = self.maxsp
        self.mp = self.maxmp


    
    def battle(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            plySpd = self.speed + random.randint(0, 100)
            enSpd = enemy.spd + random.randint(0, 100)
            turn = (plySpd > enSpd)
            if turn:
                while turn:
                    print("Your Health: " + str(self.hp) + " Stamina: " + str(self.sp) + " Mana Pool: " + str(self.mp))
                    print("%s's Health: "%enemy.name + str(enemy.hp))
                    
                    print("1. Normal Attack")
                    print("2. Strong attack")
                    #print("3. Cast a spell")
                    print("3. Use Item")
                    try:
                        inp = int(input(">"))
                    except:
                        utils.p("Please type a valid number.")
                        continue
                    
                    if inp == 1:
                        while 1:
                            for i in range(0, len(self.inventory)):
                                print(("%s.) " % str(i + 1)) + self.weapons[i].name)
                            utils.p("What weapon would you like to use? Type 'exit' to quit.")
                            inp = input(">")

                            try:
                                inp = int(inp)
                            except:
                                if inp.lower() == "exit": break

                            try:
                                self.attack(enemy, self.weapons[inp - 1])
                                
                                turn = 0
                                break
                            except:
                                utils.p("Please type a valid number.")
                    elif inp == 2:
                        if self.sp >= 15:
                            while 1:
                                for i in range(0, len(self.inventory)):
                                    print(("%s.) " % str(i + 1)) + self.weapons[i].name)
                                utils.p("What weapon would you like to use? Type 'exit' to quit.")
                                inp = input(">")

                                try:
                                    inp = int(inp)
                                except:
                                    if inp.lower() == "exit": break
                                    else:
                                        utils.p("Please type a number.")
                                        continue

                                try:
                                    self.attack(enemy, self.weapons[inp - 1], 2)
                                    self.sp -= 15
                                    turn = 0
                                    break
                                except:
                                    utils.p("Please type a valid number.")
                        else:
                            utils.p("You are too low on stamina!")
                    elif inp == 3:
                        while 1:
                            for i in range(0, len(self.inventory)):
                                print(("%s.) " % str(i + 1)) + self.inventory[i].name)
                            utils.p("What would you like to use? Type 'exit' to quit.")
                            inp = input(">")

                            try:
                                inp = int(inp)
                            except:
                                if inp.lower() == "exit": break

                            try:
                                self.inventory[inp - 1].use()
                                turn = 0
                                break
                            except:
                                utils.p("Please type a valid number.")
            if enemy.hp <= 0:
                utils.p("Defeated the %s!" %enemy.name)
                break
            
            enemy.attack()

            if self.hp <= 0:
                utils.p("You lost the fight!")
                break

            turn = 1



    
    

        

    

        

player = Player()