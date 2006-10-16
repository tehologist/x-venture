#@+leo-ver=4-thin
#@+node:234.20061005221733:@thin .\\Tests\\mudParseTest.py
#@<< docstring >>
#@+middle:234.20061005231611.1:headers_footers
#@+node:234.20061005224507:<< docstring >>
"""These are unit tests for testing mudParser module."""
#@-node:234.20061005224507:<< docstring >>
#@-middle:234.20061005231611.1:headers_footers
#@nl
#@@language python
#@@tabwidth -4
#@<< imports >>
#@+middle:234.20061005231611.1:headers_footers
#@+node:234.20061005224507.1:<< imports >>
from Lib.mudParser import mudparse
import unittest
#@nonl
#@-node:234.20061005224507.1:<< imports >>
#@-middle:234.20061005231611.1:headers_footers
#@nl
#@<< instance >>
#@+middle:234.20061005231611.1:headers_footers
#@+node:234.20061005224507.2:<< instance >>
inst = mudparse()
#@nonl
#@-node:234.20061005224507.2:<< instance >>
#@-middle:234.20061005231611.1:headers_footers
#@nl
#@+others
#@+node:234.20061005231611.1:headers_footers
#@-node:234.20061005231611.1:headers_footers
#@+node:234.20061005231611.2:testcases
#@+node:234.20061005225017.1:stripcapTestCase
class stripcapTestCase(unittest.TestCase):
    def runTest(self):
        sentence = "look at the purple bird house"
        assert inst.stripcap(sentence) == ["LOOK","AT","PURPLE","BIRD","HOUSE"],"It's Broke Dude."
        
#@-node:234.20061005225017.1:stripcapTestCase
#@+node:234.20061005225913.3:getverbTestCase
class getverbTestCase(unittest.TestCase):
    def runTest(self):
        sentence = ["LOOK","AT","PURPLE","BIRD","HOUSE"]
        assert inst.getverb(sentence) == ["LOOK",["AT","PURPLE","BIRD","HOUSE"]],"It's Broke Dude."
#@-node:234.20061005225913.3:getverbTestCase
#@+node:234.20061005230753:getprepTestCase
class getprepTestCase(unittest.TestCase):
    def runTest(self):
        sentence = ["AT","PURPLE","BIRD","HOUSE"]
        assert inst.getprep(sentence) == ["AT",["PURPLE","BIRD","HOUSE"]],inst.getprep(sentence)
#@nonl
#@-node:234.20061005230753:getprepTestCase
#@+node:234.20061008183117:getprepTestCase2
class getprepTestCase2(unittest.TestCase):
    def runTest(self):
        sentence = ["PURPLE","BIRD","HOUSE"]
        assert inst.getprep(sentence) == [None,["PURPLE","BIRD","HOUSE"]],"It's Broke Dude."
#@-node:234.20061008183117:getprepTestCase2
#@+node:234.20061005231041:getnounTestCase
class getnounTestCase(unittest.TestCase):
    def runTest(self):
        sentence = ["PURPLE","BIRD","HOUSE"]
        assert inst.getnoun(sentence) == [["PURPLE","BIRD","HOUSE"],None],inst.getnoun(sentence)
        
#@nonl
#@-node:234.20061005231041:getnounTestCase
#@+node:234.20061012164700:getnounTestCase2
class getnounTestCase2(unittest.TestCase):
    def runTest(self):
        sentence = ["PURPLE","BIRD","HOUSE","AT","MOVIES"]
        assert inst.getnoun(sentence) == [["PURPLE","BIRD","HOUSE"],["AT","MOVIES"]],"It's Broke Dude."
#@nonl
#@-node:234.20061012164700:getnounTestCase2
#@+node:234.20061005231344:parsemainTestCase
class parsemainTestCase(unittest.TestCase):
    def runTest(self):
        sentence = "Look at the purple bird house"
        assert inst.parsemain(sentence) == {'indirectnoun': None, 'indirectprep': None, 'directnoun': ['PURPLE', 'BIRD', 'HOUSE'], 'verb': 'LOOK', 'directprep': 'AT', 'args': None},inst.parsemain(sentence)
#@nonl
#@-node:234.20061005231344:parsemainTestCase
#@+node:234.20061012181240:parsemainTestCase2
class parsemainTestCase2(unittest.TestCase):
    def runTest(self):
        sentence = "Look"
        assert inst.parsemain(sentence) == {'indirectnoun': None, 'indirectprep': None, 'directnoun': None, 'verb': 'LOOK', 'directprep': None, 'args': None, 'directnoun': None},inst.parsemain(sentence)
#@-node:234.20061012181240:parsemainTestCase2
#@+node:234.20061013000604:parsemainTestCase3
class parsemainTestCase3(unittest.TestCase):
    def runTest(self):
        sentence = "Look at the purple bird house on the green table"
        assert inst.parsemain(sentence) == {'indirectnoun': ['GREEN', 'TABLE'], 'indirectprep': 'ON', 'directnoun': ['PURPLE', 'BIRD', 'HOUSE'], 'verb': 'LOOK', 'directprep': 'AT', 'args': None},inst.parsemain(sentence)
#@nonl
#@-node:234.20061013000604:parsemainTestCase3
#@+node:234.20061013001915:parsemainTestCase4
class parsemainTestCase4(unittest.TestCase):
    def runTest(self):
        sentence = "Look at the purple bird house on"
        assert inst.parsemain(sentence) == {'indirectnoun': None, 'indirectprep': 'ON', 'directnoun': ['PURPLE', 'BIRD', 'HOUSE'], 'verb': 'LOOK', 'directprep': 'AT', 'args': None},inst.parsemain(sentence)
#@nonl
#@-node:234.20061013001915:parsemainTestCase4
#@+node:234.20061012154215:preparseTestCase
class preparsemainTestCase(unittest.TestCase):
    def runTest(self):
        sentence = "say look at me"
        assert inst.preparse(sentence)[1] == {"verb":"SAY","directprep":None,"directnoun":None,"indirectprep":None,"indirectnoun":None,"args":"LOOK AT ME"},inst.preparse(sentence)
#@nonl
#@-node:234.20061012154215:preparseTestCase
#@+node:234.20061012172432:preparseTestCase2
class preparsemainTestCase2(unittest.TestCase):
    def runTest(self):
        sentence = "look at me"
        assert inst.preparse(sentence) == [["AT","ME"], {"verb":"LOOK","directprep":None,"directnoun":None,"indirectprep":None,"indirectnoun":None,"args":None}],inst.preparse(sentence)
#@nonl
#@-node:234.20061012172432:preparseTestCase2
#@-node:234.20061005231611.2:testcases
#@-others
#@<< main >>
#@+middle:234.20061005231611.1:headers_footers
#@+node:234.20061005225017:<< main >>
if __name__ == "__main__":
    unittest.main()
#@nonl
#@-node:234.20061005225017:<< main >>
#@-middle:234.20061005231611.1:headers_footers
#@nl
#@nonl
#@-node:234.20061005221733:@thin .\\Tests\\mudParseTest.py
#@-leo
