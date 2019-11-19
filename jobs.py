class Job:
    def __init__(self, name):
        self.affinities = []
        self.abilityGains = [1, 10, 30, 70, 100]
        self.abilities = []
        self.name = name

class Fighter(Job):
    def __init__(self):
        super().__init__("Fighter")

class Thief(Job):
    def __init__(self):
        super().__init__("Thief")

class Monk(Job):
    def __init__(self):
        super().__init__("Monk")

class Mage(Job):
    def __init__(self):
        super().__init__("Mage")

class Archer(Job):
    def __init__(self):
        super().__init__("Archer")
