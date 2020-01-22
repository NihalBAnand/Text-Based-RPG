from locations.location import Location
from locations.buildings.falaria_buildings import *

class Falaria(Location):
    def __init__(self):
        super().__init__(5, 5, [Guild()])
    
    def enterF(self):
        p("The stylish, modern city of Falaria meets your eyes.", space=1)
        p("Well, as modern as a middle ages European setting can get, anyway.", space=.5)
        p("It has aqueducts!..", space=0.5)
        p("...", 1, 1)
        p("Well, who cares, it's the starting town. Get on with it.")
        super().enter()
	
    def enter(self):
        p("Welcome back to Falaria!")
        super().enter()
