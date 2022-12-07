from game import event
import random
from game.combat import Combat
from game.combat import Drowned
from game.display import announce

class DavyJones (event.Event):

    def __init__ (self):
        self.name = " Davy Jones attack"

    def process (self, world):
        result = {}
        result["message"] = "Davy Jones has been defeated! He left a note!"
        monsters = []
        min = 2
        uplim = 6
        if random.randrange(2) == 0:
            min = 1
            uplim = 5
            monsters.append(Drowned("Pirate captain"))
            monsters[0].speed = 1.2*monsters[0].speed
            monsters[0].health = 2*monsters[0].health
        n_appearing = random.randrange(min, uplim)
        n = 1
        while n <= n_appearing:
            monsters.append(Drowned("Drowned pirate "+str(n)))
            n += 1
        announce ("You are attacked by a crew of drowned pirates!")
        Combat(monsters).combat()
        result["newevents"] = [ self ]
        return result
