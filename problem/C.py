
# _IDs_ holds the name (identification) of the matters in concern.
_IDs_ = ["Frank Hall", "George Kirk", "Mark Tyrone",
         "Paul Gregory", "Steve O'Hara"]
#     _Attributes_ holds a list of String-List pair, where each string
# represents an attribute in concern, and the list holds all possible
# values for that attribute.
_Attributes_ = [["number", [16, 20, 24, 32, 36]],
                ["day", [1, 2, 4, 5, 6]],
                ["food", ["Hot Dog", "Pretzel", "Ice Cream", "Peanut", "Cracker Jack"]]]

# The class holds the structure of the subjects in concern.
class Subject(object):
    def __init__(self, number, day, food, name):
        self.number = number
        self.day = day
        self.food = food
        self.name = name
        # Carry over information from Part A and Part B.
        if name == "Steve O'Hara":
            self.avg = 305
            self.posi = "A"
            self.team = "Tip-Tops"
            self.position = "Catcher"
        elif name == "Paul Gregory":
            self.avg = 295
            self.posi = "D"
            self.team = "Rebels"
            self.position = "Center Fielder"
        elif name == "George Kirk":
            self.avg = 290
            self.posi = "C"
            self.team = "Whales"
            self.position = "Left Fielder"
        elif name == "Mark Tyrone":
            self.avg = 310
            self.posi = "B"
            self.team = "Federals"
            self.position = "Third Baseman"
        elif name == "Frank Hall":
            self.avg = 315
            self.posi = "E"
            self.team = "Terrapins"
            self.position = "Shortstop"
        else:   # Should not happen!
            tmp = 1 / 0 

#    The _validate_ function holds a dictionary of objects, indexed by
# the IDs of the objects.
def _validate_(soln):
    try:
        # Start checking the clues.
        # Clue One.
        Catcher = locate_obj(soln, "position", "Catcher")
        HotDogGuy = locate_obj(soln, "food", "Hot Dog")
        assert(Catcher.day - 1 == HotDogGuy.day)
        assert(Catcher.number - 4 == HotDogGuy.number)
        # Clue Two.
        MVP_W = locate_obj(soln, "team", "Whales")
        PretzelGuy = locate_obj(soln, "food", "Pretzel")
        assert(MVP_W.number - 4 == PretzelGuy.number)
        assert(PretzelGuy.day > 1)
        # Clue Three.
        for obj in _IDs_:
            if soln[obj].food == "Ice Cream":
                IceCreamGuy = soln[obj]
            if soln[obj].food == "Peanut":
                PeanutGuy = soln[obj]
        assert(locate_obj(soln, "food", "Ice Cream").number + 4 == locate_obj(soln, "food", "Peanut").number)
        # Clue Four.
        CenterFielder = locate_obj(soln, "position", "Center Fielder")
        MVP_Terr = locate_obj(soln, "team", "Terrapins")
        assert(CenterFielder.number - 8 == MVP_Terr.number)
        assert(CenterFielder.day + 2 == MVP_Terr.day)
        # Clue Five.
        CrackerJackGuy = locate_obj(soln, "food", "Cracker Jack")
        MondayGuy = locate_obj(soln, "day", 1)
        assert(CrackerJackGuy.number - 4 == MondayGuy.number)
    except AssertionError:
        return False
    except:
        print "Error occured while validating tentative solution."
        sys.exit(1)
    else:
        return True

# DO NOT modify this segment.
def locate_obj(dictionary, attr_name, attr_value):
    for k in dictionary:
        if getattr(dictionary[k], attr_name) == attr_value:
            return dictionary[k]
    return 1/0  # Should not happen!

