from game import event
from game.player import Player
from game.context import Context
import game.config as config
import random

class Bats (Context, event.Event):

    def __init__ (self):
        super().__init__()
        self.name = "bat visitor"
        self.bats = 1
        self.verbs['chase'] = self
        self.verbs['feed'] = self
        self.verbs['help'] = self
        self.result = {}
        self.go = False

    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "chase"):
            self.go = True
            r = random.randint(1,10)
            if (r < 5):
                self.result["message"] = "the Candy bats fly off."
                if (self.bats > 1):
                    self.bats = self.bats - 1
            else:
                c = random.choice(config.the_player.get_pirates())
                if (c.lucky == True):
                    self.result["message"] = "luckly, the Candy bats fly off."
                else:
                    self.result["message"] = c.get_name() + " is attacked by the Candy bats."
                    if (c.inflict_damage (self.bats, "swarmed to death by Candy bats")):
                        self.result["message"] = ".. " + c.get_name() + " is pecked to death by the Candy bats!"

        elif (verb == "feed"):
            self.bats = self.bats + 1
            self.result["newevents"].append (bat())
            self.result["message"] = "the Candy bats are happy"
            self.go = True
        elif (verb == "help"):
            print ("the Candy bats will pester you until you feed them or chase them off")
            self.go = False
        else:
            print ("it seems the only options here are to feed or chase")
            self.go = False



    def process (self, world):

        self.go = False
        self.result = {}
        self.result["newevents"] = [ self ]
        self.result["message"] = "default message"

        while (self.go == False):
            print (str (self.bats) + " Candy bats have appeared what do you want to do?")
            Player.get_interaction ([self])

        return self.result
