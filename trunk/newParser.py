from pyparsing import *

class AppParseException(ParseException):
    pass

class parser(object):
    def __init__(self):
        self.bnf = self.makeBNF()

    def makeBNF(self):
        partofspeech = CaselessKeyword("IN") | CaselessKeyword("ON") | CaselessKeyword("BY")
        prs = Word(alphas) + SkipTo(White() + partofspeech) + partofspeech + restOfLine
        prs2 = Word(alphas) + partofspeech + restOfLine
        prs3 = Word(alphas) + restOfLine
        return ( prs | prs2 | prs3 )

    def parseCmd(self, cmdstr):
        try:
            ret = self.bnf.parseString(cmdstr)
            return ret
        except AppParseException, pe:
            print pe.msg
        except ParseException, pe:
            print "WTF?"