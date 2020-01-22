from weapons import *

class Job:
    def __init__(self, name):
        self.affinities = []
        self.abilityGains = [1, 10, 30, 70, 100]
        self.abilities = []
        self.name = name

class Fighter(Job):
    def __init__(self):
        super().__init__("Fighter")
        self.affinities = [Longsword(), Shortbow()]


class Thief(Job):
    def __init__(self):
        super().__init__("Thief")
        self.affinities = [Knife()]

class Monk(Job):
    def __init__(self):
        super().__init__("Monk")
        self.affinities = [Staff(), Nunchuks()]


class Mage(Job):
    def __init__(self):
        super().__init__("Mage")
        self.affinities = [Staff()]

class Archer(Job):
    def __init__(self):
        super().__init__("Archer")
        self.affinities = [Shortbow(), Knife()]
