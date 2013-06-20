#!/usr/bin/env python
import sys
import imp
import itertools

# Load the puzzle criteria file.
if len(sys.argv) != 2:
    print "Usage:\t ./solve.py FILE_NAME_TO_SPEC."
    sys.exit(1)

try:
    _temp = imp.load_source("criteria", sys.argv[1])
    _IDs_ = _temp._IDs_
    _Attributes_ = _temp._Attributes_
    Subject = _temp.Subject
    _validate_ = _temp._validate_
except:
    print "Malformed SPEC file!"
    sys.exit(1)

# Check the possibilities.
print "Configuration filename:", sys.argv[1]
print "-" * 20, "START SOLVING", "-" * 20
soln_count = 0
profiles = [[] for i in xrange(len(_Attributes_))]
for i in xrange(len(_Attributes_)):
    profiles[i] = itertools.permutations(_Attributes_[i][1])

for config in itertools.product(*profiles):
    tmpdict = dict()
    options = zip(*config)
    for i in xrange(len(_IDs_)):
        tmpdict[_IDs_[i]] = Subject(*(options[i] + (_IDs_[i],)))
    # We got a solution!
    if _validate_(tmpdict):
        soln_count += 1
        print "Solution", soln_count, "found."
        for subj in tmpdict.keys():
            print subj, "\t",
            for attr in _Attributes_:
                print str(attr[0]) + ":", getattr(tmpdict[subj], attr[0]), "\t",
            print
        print "Press ENTER to continue..."
        raw_input()

print "Solving complete! Found", soln_count, "solution(s) in total."
print "Thank you for using Logic-Problem-Solver by Jimmy!"
