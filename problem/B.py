
# _IDs_ holds the name (identification) of the matters in concern.
_IDs_ = ["Frank Hall", "George Kirk", "Mark Tyrone",
         "Paul Gregory", "Steve O'Hara"]
#     _Attributes_ holds a list of String-List pair, where each string
# represents an attribute in concern, and the list holds all possible
# values for that attribute.
_Attributes_ = [["team", ["Federals", "Rebels", "Terrapins", "Tip-Tops", "Whales"]],
                ["position", ["Catcher", "Center Fielder", "Left Fielder", "Shortstop", "Third Baseman"]]]

# The class holds the structure of the subjects in concern.
class Subject(object):
    def __init__(self, team, position, name):
        self.team = team
        self.position = position
        # Carry over information from Part A.
        if name == "Steve O'Hara":
            self.avg = 305
            self.posi = "A"
        elif name == "Paul Gregory":
            self.avg = 295
            self.posi = "D"
        elif name == "George Kirk":
            self.avg = 290
            self.posi = "C"
        elif name == "Mark Tyrone":
            self.avg = 310
            self.posi = "B"
        elif name == "Frank Hall":
            self.avg = 315
            self.posi = "E"
        else:   # Should not happen!
            tmp = 1 / 0 

#    The _validate_ function holds a dictionary of objects, indexed by
# the IDs of the objects.
def _validate_(soln):
    try:
        # Start checking the clues.
        # Clue One.
        for obj in _IDs_:
            if soln[obj].avg == 310:
                MVP_F = soln[obj]
            if soln[obj].position == "Catcher":
                Catcher = soln[obj]
                CatcherName = obj
        assert(MVP_F.team == "Federals")
        assert(abs(ord(MVP_F.posi) - ord(Catcher.posi)) == 1)
        assert(CatcherName != "George Kirk")
        # Clue Two.
        for obj in _IDs_:
            if soln[obj].position == "Center Fielder":
                CenterF = soln[obj]
            elif soln[obj].position == "Left Fielder":
                LeftF = soln[obj]
        assert(CenterF.team == "Rebels")
        assert(CenterF.avg - 5 == LeftF.avg)
        assert(LeftF.posi != "B")
        # Clue Three.
        for obj in _IDs_:
            if soln[obj].position == "Third Baseman":
                ThirdBase = soln[obj]
            if soln[obj].team == "Terrapins":
                MVP_Terr = soln[obj]
        assert(ThirdBase.avg < MVP_Terr.avg)
        # Clue Four.
        for obj in _IDs_:
            if soln[obj].team == "Whales":
                assert(soln[obj].posi != "A")
    except AssertionError:
        return False
    #except:
    #    print "Error occured while validating tentative solution."
    #    sys.exit(1)
    else:
        return True

