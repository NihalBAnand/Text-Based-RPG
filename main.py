from utils import *
from playa import *
from races import *
from person import *
from locations.location import *
from jobs import *
from locations.falaria import *
from enemies import *


#Intro
clear()

print("Enter Code")
code = input(">").lower()
if code == "end":
    player.job = Mage()
    player.affinities = player.job.affinities
    for weapon in player.affinities:
        player.inventory.append(weapon)
        player.weapons.append(weapon)
    Falaria().enter()

elif code == "battle":
    player.job = Fighter()
    player.affinities = player.job.affinities
    for weapon in player.affinities:
        player.inventory.append(weapon)
        player.weapons.append(weapon)
    player.battle(Zombie())
    player.overworld()

elif code == "skip":
    pass
else:

    p("Hello! My name is ������!")
    p("Huh?", space = 0.5)
    p("You couldn't read that?", space = 0.5)
    p("I guess my language is untintelligble to humans.")
    p("Anyway, I'm a being that you would call a god of some sort.")
    p("But, I would rather call myself a Game Master.")    
    p("...", 0.5, 1)
    p("Well, you don't really exist yet.")
    p("As a special service, I'll allow you to decide what you are.")
    p("Now, you should pick your race.")

#Pick Race
races = [HighElf(), DarkElf(), Dwarf(), HalfOrc(), Aarakocra(), Human(), Lizalfos()]
while 1:
    print("1.) High Elf")
    print("2.) Dark Elf")
    print("3.) Dwarf")
    print("4.) Half-Orc")
    print("5.) Aarakocra")
    print("6.) Human")
    print("7.) Lizalfos")
    try:
        inp = int(input(">"))
    except:
        p("Please type a number.")
        continue
    p(races[inp - 1].intro)
    p("Are you sure you want to choose to be a %s? (y or n)" % races[inp - 1].name)
    inp2 = input(">").lower()
    if inp2 == "y":
        player.race = races[inp - 1]
        player.race.bonus += player.race.levelUp()
        break
    else:
        continue



#Pick Name
while 1:
    p("And, what's your name?")
    player.name = input(">")
    p("Are you sure? (y/n)")
    test = input(">").lower()
    if test == "y":
        break
    else:
        continue

p("Hello, %s!" % player.name)

    


#Pick job!
jobs = [Fighter(), Thief(), Monk(), Mage(), Archer()]
p("At this point you should pick your job.")
while 1:
    print("1.) Fighter")
    print("2.) Thief")
    print("3.) Monk")
    print("4.) Mage")
    print("5.) Archer")
    try:
        inp = int(input(">"))
        p("Are you sure? (y or n)")
        inp2 = input(">").lower()
        if inp2 == "y":
            break
        else:
            continue
    except:
        p("Please type a number.")
player.job = jobs[inp - 1]
player.affinities = player.job.affinities
for weapon in player.affinities:
    player.inventory.append(weapon)
    player.weapons.append(weapon)


#GO!
p("You are about to enter a world of magic, wonder, and text-based beauty. Are you ready to jump into this? (y or n)")
inp = input(">").lower()
if inp == "y":
    p("Good! Now, you're going to the town of Falaria. Enjoy yourself!")
elif inp == "n":
    p("Too bad, so sad. You probably shouldn't have picked this game. Now, you're going to the town of Falaria. Enjoy yourself!")
else:
    p("I don't know what you were trying to say, but I'm still annoyed. Now, you're going to the town of Falaria.")
time.sleep(3)
clear()

Falaria().enterF()


