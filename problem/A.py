
# _IDs_ holds the name (identification) of the matters in concern.
_IDs_ = ["Frank Hall", "George Kirk", "Mark Tyrone",
         "Paul Gregory", "Steve O'Hara"]
#     _Attributes_ holds a list of String-List pair, where each string
# represents an attribute in concern, and the list holds all possible
# values for that attribute.
_Attributes_ = [["avg", [290, 295, 305, 310, 315]],
                ["position", ["A", "B", "C", "D", "E"]]]

# The class holds the structure of the subjects in concern.
class Subject(object):
    def __init__(self, avg, position, name):
        self.avg = avg
        self.position = position

#    The _validate_ function holds a dictionary of objects, indexed by
# the IDs of the objects.
def _validate_(soln):
    try:
        # Start checking the clues.
        # Clue One.
        assert(ord(soln["Steve O'Hara"].position) + 1 == ord(soln["Mark Tyrone"].position))
        assert(soln["Mark Tyrone"].avg - soln["Steve O'Hara"].avg == 5)
        # Clue Two.
        assert(ord(soln["George Kirk"].position) + 1 == ord(soln["Paul Gregory"].position))
        assert(soln["George Kirk"].position != "D")
        assert(soln["Paul Gregory"].avg - soln["George Kirk"].avg == 5)
        # Clue Three.
        assert(soln["Paul Gregory"].position != "B")
        for obj in _IDs_:
            if soln[obj].position == "B":
                assert(soln["Frank Hall"].avg - soln[obj].avg == 5)
    except AssertionError:
        return False
    except:
        print "Error occured while validating tentative solution."
        sys.exit(1)
    else:
        return True

