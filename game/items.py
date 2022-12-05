
class Item():
    def __init__(self, name, value):
        super().__init__()
        self.name = name
        self.value = value
        self.damage = (0,0)
        self.firearm = False
        self.charge = False
        self.skill = None
        self.verb = None
        self.verb2 = None

    def __str__(self):
        return self.name + " (" + str(self.value) + " shillings)"

    def __lt__(self, other):
        return self.name < other.name

    def value(self):
        return self.value

class Cutlass(Item):
    def __init__(self):
        super().__init__("cutlass", 5) #Note: price is in shillings (a silver coin, 20 per pound)
        self.damage = (10,60)
        self.skill = "swords"
        self.verb = "cut"
        self.verb2 = "slashes"

class Flintlock(Item):
    def __init__(self):
        super().__init__("flintlock", 400) #Note: price is in shillings (a silver coin, 20 per pound)
        self.damage = (10,100)
        self.firearm = True
        self.charge = True
        self.skill = "guns"
        self.verb = "shoot"
        self.verb2 = "shoots"

class Lightsaber(Item):
    def __init__(self):
        super().__init__("lightsaber", 750)
        self.damage = (25,100)
        self.skill = "saber"
        self.verb = "stab"
        self.verb2 = "severs"

class MarshmellowGun(Item):
    def __init__(self):
        super().__init__("marshmellow gun") #Note: price is in shillings (a silver coin, 20 per pound)
        self.damage = (100,100)
        self.firearm = True
        self.charge = True
        self.skill = "shooter"
        self.verb = "pew"
        self.verb2 = "mellows"
        
