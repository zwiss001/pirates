
from game import location
from game import config
from game.display import announce
from game.events import *
from game.items import Lightsaber
from game.items import MarshmellowGun

class CandyIsland (location.Location):

    def __init__ (self, x, y, w):
        super().__init__(x, y, w)
        self.name = "candy island"
        self.symbol = 'CI'
        self.visitable = True
        self.starting_location = Shore_with_ship(self)
        self.locations = {}
        self.locations["sugar shore"] = self.starting_location
        self.locations["Lollypoptrees"] = LollypopTrees(self)
        self.locations["CandyRockCave"] = CandyRockCave(self)

    def enter (self, ship):
        print ("\nThe crew arrived at a candy island")

    def visit (self):
        config.the_player.location = self.starting_location
        config.the_player.location.enter()
        super().visit()

class Shore_with_ship (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "sugar shore"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self
        self.event_chance = 50
        self.events.append (bats.Bats())

    def enter (self):
        announce ("the crew arrives at the sugar shore at the south of the island.")
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            announce ("You return to your ship.")
            config.the_player.next_loc = config.the_player.ship
            config.the_player.visiting = False
        elif (verb == "north"):
            config.the_player.next_loc = self.main_location.locations["Lollypoptrees"]
        elif (verb == "east"):
            announce ("You walk around and see a chocolate lake. There is nothing to do with it.")
        elif (verb == "west"):
            config.the_player.next_loc = self.main_location.locations["CandyRockCave"]

class CandyRockCave(location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "CandyRockCave"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        

        self.event_chance = 50
        self.events.append(DavyJonesBoss.DavyJones())

    def enter (self):
        description="You walk into a Rock Candy Cave. It is very dark. You see a GummyBear in the cave."
        DavyJonesBoss.DavyJones().process(config.the_player.world)

    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south" or verb == "north" or verb == "east" or verb == "west"):
            config.the_player.next_loc = self.main_location.locations["sugar shore"]
        
class LollypopTrees (location.SubLocation):
    def __init__ (self, m):
        super().__init__(m)
        self.name = "Lollypoptrees"
        self.verbs['north'] = self
        self.verbs['south'] = self
        self.verbs['east'] = self
        self.verbs['west'] = self

        # Include a couple of items and the ability to pick them up, for demo purposes
        self.verbs['take'] = self
        self.item_in_tree = Lightsaber()

    def enter (self):
        description="You walk into the Lollypop Forest on the island."
        if self.item_in_tree != None:
            description = description + " You see a " + self.item_in_tree.name + " stuck in a Lollypoptree."
        announce (description)
    
    def process_verb (self, verb, cmd_list, nouns):
        if (verb == "south"):
            config.the_player.next_loc = self.main_location.locations["sugar shore"]
        #Handle taking items. Demo both "take cutlass" and "take all"
        if verb == "take":
            if self.item_in_tree == None:
                announce ("You don't see anything to take.")
            elif len(cmd_list) > 1:
                at_least_one = False #Track if you pick up an item, print message if not.
                item = self.item_in_tree
                if item != None and (cmd_list[1] == item.name or cmd_list[1] == "all"):
                    announce ("You take the "+item.name+" from the tree.")
                    config.the_player.add_to_inventory([item])
                    self.item_in_tree = None
                    config.the_player.go = True
                    at_least_one = True
                if at_least_one == False:
                    announce ("You don't see one of those around.")
        if (verb =="north"):
            announce("The crew sees a great view upon a chocolate mountaintop! There is nothing for them there.")
            config.the_player.next_loc = self.main_location.locations["sugar shore"]

        if (verb =="west"):
            announce("The crew sees a Rock Candy Cave! They go down to explore!")
            config.the_player.next_loc = self.main_location.locations["CandyRockCave"]
        if (verb =="east"):
            announce("The crew sees a soda waterfall! There is nothing for them there.")
            config.the_player.next_loc = self.main_location.locations["sugar shore"]

            
