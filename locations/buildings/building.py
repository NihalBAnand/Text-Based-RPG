from utils import *

class Building:
    def __init__(self, major=False, item=None):
        self.major = major
        self.name = ""
    
    def enter(self):
        if self.item==None and not self.major:
            p("There's nothing here that looks useful.")
    