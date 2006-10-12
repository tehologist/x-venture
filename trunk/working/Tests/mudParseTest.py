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
        assert inst.getprep(sentence) == ["AT",["PURPLE","BIRD","HOUSE"]],"It's Broke Dude."
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
        assert inst.getnoun(sentence) == [["PURPLE","BIRD","HOUSE"],None],"It's Broke Dude."
#@nonl
#@-node:234.20061005231041:getnounTestCase
#@+node:234.20061005231344:parsemainTestCase
class parsemainTestCase(unittest.TestCase):
    def runTest(self):
        sentence = "Look at the purple bird house"
        assert inst.parsemain(sentence) == {"verb":"LOOK","directprep":"AT","directnoun":["PURPLE","BIRD","HOUSE"]},"It's Broke Dude."
#@nonl
#@-node:234.20061005231344:parsemainTestCase
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
