from game import event
import random
from game.combat import Combat
from game.combat import Davyjones
from game.display import announce
from game.ship import *
from game import config

class DavyJones (event.Event):

    def __init__ (self):
        self.name = " Davy Jones attack"

    def process (self, world):
        result = {}
        
        monsters = []
        monsters.append(Davyjones("Davy Jones"))
        monsters[0].speed = 4*monsters[0].speed
        monsters[0].health = 25*monsters[0].health
        announce ("You are attacked by the Great Davy Jones")
        Combat(monsters).combat()
        result["message"] = "Davy Jones has been defeated! He left a note!"
        announce("The note says the coordinates of the homeport:"+ str(config.the_player.world.homex)+", "+str(config.the_player.world.homey))
        result["newevents"] = [ self ]
        return result
