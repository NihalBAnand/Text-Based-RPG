from playa import player

class Spell:
    def __init__(self, dmg, name, msg, accur, mp):
        self.dmg = dmg #should be between 7 and 50
        self.name = name
        self.msg = msg
        self.accur = accur #between 1 and 256
        self.mp = mp

class Fireball(Spell):
    def __init__(self):
        super().__init__(7, "Fireball", "You summon a mighty fireball to strike your foe.", 150, 15)


class IceSpear(Spell):
    def __init__(self):
        super().__init__(10, "Ice Spear", "You conjure a frozen blade of ice to pierce your foe.", 75, 15)

class LightningBolt(Spell):
    def __init__(self):
        super().__init__(5, "Lightning Bolt", "Lightning bursts from your fingers to shock your foe.", 256, 15)



