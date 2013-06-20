
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
        for obj in _IDs_:
            if soln[obj].position == "Catcher":
                Catcher = soln[obj]
            if soln[obj].food == "Hot Dog":
                HotDogGuy = soln[obj]
        assert(Catcher.day - 1 == HotDogGuy.day)
        assert(Catcher.number - 4 == HotDogGuy.number)
        # Clue Two.
        for obj in _IDs_:
            if soln[obj].team == "Whales":
                MVP_W = soln[obj]
            if soln[obj].food == "Pretzel":
                PretzelGuy = soln[obj]
        assert(MVP_W.number - 4 == PretzelGuy.number)
        assert(PretzelGuy.day > 1)
        # Clue Three.
        for obj in _IDs_:
            if soln[obj].food == "Ice Cream":
                IceCreamGuy = soln[obj]
            if soln[obj].food == "Peanut":
                PeanutGuy = soln[obj]
        assert(IceCreamGuy.number + 4 == PeanutGuy.number)
        # Clue Four.
        for obj in _IDs_:
            if soln[obj].position == "Center Fielder":
                CenterFielder = soln[obj]
            if soln[obj].team == "Terrapins":
                MVP_Terr = soln[obj]
        assert(CenterFielder.number - 8 == MVP_Terr.number)
        assert(CenterFielder.day + 2 == MVP_Terr.day)
        # Clue Five.
        for obj in _IDs_:
            if soln[obj].food == "Cracker Jack":
                CrackerJackGuy = soln[obj]
            if soln[obj].day == 1:
                MondayGuy = soln[obj]
        assert(CrackerJackGuy.number - 4 == MondayGuy.number)
    except AssertionError:
        return False
    except:
        print "Error occured while validating tentative solution."
        sys.exit(1)
    else:
        return True

