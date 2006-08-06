import mudgrammar as MG
from pyparsing import *

class AppParseException(ParseException):
    pass

class parser(object):
    def __init__(self):
        self.bnf = self.makeBNF()

    def makeBNF(self):
        return ( MG.cmdSay |
            MG.cmdLook |
            MG.cmdInv |
            MG.cmdMove |
            MG.cmdTake |
            MG.cmdDrop |
            MG.cmdDrop |
            MG.cmdQuit )

    def parseCmd(self, cmdstr):
        try:
            ret = self.bnf.parseString(cmdstr)
            return ret
        except AppParseException, pe:
            print pe.msg
        except ParseException, pe:
            print "WTF?"