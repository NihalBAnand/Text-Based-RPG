import utils
import playa
import random

class Enemy:
    def __init__(self, hp, mp, sp, spd, defse, atk, typ, accur):
        self.hp = hp
        self.mp = mp
        self.sp = sp
        self.spd = spd
        self.defse = defse
        self.atk = atk #generally between 10 and 100 based on difficulty
        self.typ = typ #1 - fight, 2 - magic
        self.accur = accur #MAX 256
    
    def attack(self):
        agi = random.randint(1, 50)
        temptype = self.typ
        if agi > 49:
            if self.typ == 1:
                temptype = 2
            else:
                temptype = 1
        
        if temptype == 1:
            move = random.randint(1, 5)
            if self.sp > 0 and move > 3:
                accur = random.randint(0, 256)
                utils.p("Your foe attempts to strike you with a powerful blow!")
                if accur < self.accur:
                    damage = (self.atk + 1) * random.randint(1, round(self.atk / 4))
                    playa.player.hp -= damage
                    utils.p("It hits you for %s damage!" %damage)
                else:
                    utils.p("It strikes the air next to you instead!")


            else:
                accur = random.randint(0, 256)
                utils.p("Your foe attempts to hit you!")
                if accur < self.accur:
                    damage = (self.atk + 1)
                    playa.player.hp -= (self.atk + 1)
                    utils.p("It hits you for %s damage" %damage)
                else:
                    utils.p("It strikes the air next to you instead!")
        elif temptype == 2:
            move = random.randint(1, 5)
            if self.sp > 0 and move > 3:
                accur = random.randint(0, 256)
                if accur < self.accur:
                    playa.player.hp -= (self.atk + 1) * random.randint(round(self.atk / 4))
                self.sp -= 10
            else:
                accur = random.randint(0, 256)
                if accur < self.accur:
                    playa.player.hp -= (self.atk + 1)
            

class Zombie(Enemy):
    def __init__(self):
        super().__init__(50, 10, 50, 3, 5, 15, 1, 256)