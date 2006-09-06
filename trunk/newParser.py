"""Module to parse and transform string into a dictionary appropriate for use
by mud engine."""
from pyparsing import *

class AppParseException(ParseException):
    pass

class mudparser(object):
    """Parses string, removes unneccessary input, uppercases, then transforms
    to dictionary"""
    
    def __init__(self):
        """Creates initial bnf"""
        self.bnf = self.makeBNF()

    def capstrip(self, cmdstr):
        """Capitalizes and strips out a, an, the"""
        teh = OneOrMore(Word(alphas) + Optional(Word(nums))).ignore(oneOf("a an the")) + Optional(Word(nums))
        stripped = teh.parseString(cmdstr)
        stripped = " ".join(stripped).upper()
        return stripped

    def makedict(self, cmdstr):
        parseresult = {'verb' : None, 'directprep' : None, 'directobj' : None, \
                       'indirectprep' : None, 'indirectobj' : None}

    def parseobject(self, arg):
        obj = Group(OneOrMore(Word(alphas))) + Optional(Word(nums))
        return obj.parseString(arg)

    def makeBNF(self):
        """Returns bnf for 3 types of sentences."""
        preposition = Keyword("IN") | Keyword("ON") | Keyword("BY")
        prs = Word(alphas) + SkipTo(White() + preposition) + preposition + restOfLine
        prs2 = Word(alphas) + preposition + restOfLine
        prs3 = Word(alphas) + LineEnd()
        prs4 = Word(alphas) + restOfLine
        return ( prs2 | prs | prs3 | prs4)

    def parseCmd(self, cmdstr):
        """Parses the actual command string and returns appropriate output"""
        strip = self.capstrip(cmdstr)
        try:
            ret = self.bnf.parseString(strip)
            return ret
        except AppParseException, pe:
            print pe.msg
        except ParseException, pe:
            print "WTF?"
