from items import *

class Weapon(Item):
    def __init__(self, dmg, name):
        self.dmg = dmg #should be between 1 and 20
        self.name = name


class Knife(Weapon):
    def __init__(self):
        super().__init__(5, "Knife")

class Longsword(Weapon):
    def __init__(self):
        super().__init__(10, "Longsword")

class Staff(Weapon):
    def __init__(self):
        super().__init__(5, "Staff")

class Shortbow(Weapon):
    def __init__(self):
        super().__init__(10, "Shortbow")

class Nunchuks(Weapon):
    def __init__(self):
        super().__init__(7, "Nunchuks")