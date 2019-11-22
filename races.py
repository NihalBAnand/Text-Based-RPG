from playa import *

class Race:
    def __init__(self, bonus):
        self.bonus = bonus
        self.ability = [1, 10, 30, 50, 100]
    
    def levelUp(self):
        return 10

class Aarakocra(Race):
    def __init__(self):
        super().__init__(player.speed)
        self.intro = "The Aarakocra are graceful bird creatures that are as fast and light as the wind."
        self.name = "Aarakocra"

class DarkElf(Race):
    def __init__(self):
        super().__init__(player.magic)
        self.name = "Dark Elf"
        self.intro = "The Dark Elves are powerful hybrids of High Elves and Humans, capable of wielding more powerful magic than either."

class Dwarf(Race):
    def __init__(self):
        super().__init__(player.maxhp)
        self.name = "Dwarf"
        self.intro = "The stoic Dwarves are renowned for their sturdiness and vitality."

class HalfOrc(Race):
    def __init__(self):
        super().__init__(player.defense)
        self.name = "Half-Orc"
        self.intro = "Half-Orcs are known for their ability to absorb damage dealt to them."

class HighElf(Race):
    def __init__(self):
        super().__init__(player.maxmp)
        self.name = "High Elf"
        self.intro = "High Elves are a proud race intertwined with magic that have an inherently higher mana pool than others."

class Human(Race):
    def __init__(self):
        super().__init__(player.maxsp)
        self.name = "Human"
        self.intro = "Humans are known for their willpower and everlasting stamina."

class Lizalfos(Race):
    def __init__(self):
        super().__init__(player.strength)
        self.name = "Lizalfos"
        self.intro = "Lizalfos are lizard creatures known for their cunning and strength."