#@+leo-ver=4-thin
#@+node:234.20061005194826:@thin .\\Lib\\mudParser.py
#@<< docstring >>
#@+middle:234.20061005231611:headers_footers
#@+node:234.20061005195515:<< docstring >>
"""This is a simple parser for a mud grammar."""
#@nonl
#@-node:234.20061005195515:<< docstring >>
#@-middle:234.20061005231611:headers_footers
#@nl
#@@language python
#@@tabwidth -4
#@<< imports >>
#@+middle:234.20061005231611:headers_footers
#@+node:234.20061005195515.1:<< imports >>
#@+at 
#@nonl
# Place any imports here.
#@-at
#@@c
from copy import copy
#@nonl
#@-node:234.20061005195515.1:<< imports >>
#@-middle:234.20061005231611:headers_footers
#@nl
#@+others
#@+node:234.20061005231611:headers_footers
#@-node:234.20061005231611:headers_footers
#@+node:234.20061005195839:class mudparse
class mudparse:
    """Create instance then pass in string which returns a dictionary."""
    def __init__(self):
        """Create dictionary."""
        self.sentstruct = {"verb": None, "directprep": None, "directnoun": None, "indirectprep": None, "indirectnoun": None,"args":None}
        self.preposition = ["IN","ON","AT"]
        
#@nonl
#@+node:234.20061012153541:preparse
    def preparse(self, cmd):
        """Parses commands to see if meet any special requirements before passing to parsemain."""
        muddict = copy(self.sentstruct)
        cmd = self.stripcap(cmd)
        verb, args = self.getverb(cmd)
        muddict["verb"] = verb
        if muddict["verb"] == "SAY":
            sentence = " ".join(args)
            muddict["args"] = sentence
        temp = []
        temp.append(args)
        temp.append(muddict)
        return temp
        
        
#@nonl
#@-node:234.20061012153541:preparse
#@+node:234.20061005200343:stripcap
    def stripcap(self, cmd):
        """Takes a string, removes instances of a, an and the, then capitalizes and returns list of all elements."""
        WHITE = " "
        BLANK = ""
        articles = ("A","AN","THE")
        cmd = cmd.upper()
        for article in articles:
            cmd = cmd.replace(article + WHITE, BLANK)
        cmd = cmd.split()
        return cmd
#@nonl
#@-node:234.20061005200343:stripcap
#@+node:234.20061005200926:getverb
    def getverb(self, cmd):
        """sets verb in dictionary to first first word in sentence. Removes first word in sentence."""
        temp = []
        temp.append(cmd[0])
        cmd.remove(cmd[0])
        temp.append(cmd)
        return temp
#@nonl
#@-node:234.20061005200926:getverb
#@+node:234.20061005203939:getprep
    def getprep(self, cmd):
        """Will return none if token is not a preposition, else will return preposition."""
        temp = []
        if len(cmd) == 0:
            temp.append(None)
            temp.append(cmd)
            return temp
        if cmd[0] in self.preposition:
            temp.append(cmd[0])
            cmd.remove(cmd[0])
            temp.append(cmd)
        else:
            temp.append(None)
            temp.append(cmd)
        return temp
#@nonl
#@-node:234.20061005203939:getprep
#@+node:234.20061005203939.1:getnoun
    def getnoun(self, cmd):
        """Will return list of all words till either list ends or element is a preposition."""
        temp =[]
        noun = []
        other = []
        prepflag = 0
        if len(cmd) == 0:
            noun.append(None)
            noun.append(cmd)
            return noun
        for word in cmd:
            if prepflag == 1:
                other.append(word)
            elif word not in self.preposition:
                temp.append(word)
            else:
                other.append(word)
                prepflag = 1
        if len(other) == 0:
            other = None
        noun.append(temp)
        noun.append(other)
        return noun
        
#@nonl
#@-node:234.20061005203939.1:getnoun
#@+node:234.20061005203939.2:parsemain
    def parsemain(self, cmd):
        """Calls functions in order and assigns elements to dict based on return."""
        temp = self.preparse(cmd)
        if temp[0] == None:
            return temp[1]
        args,muddict = temp
        prep, args = self.getprep(args)
        if prep is not None:
            muddict["directprep"] = prep
        noun, args = self.getnoun(args)
        muddict["directnoun"] = noun
        if args is not None:
            inprep, args = self.getprep(args)
            muddict["indirectprep"] = inprep
            innoun, args = self.getnoun(args)
            muddict["indirectnoun"] = innoun
            muddict["args"] = None
        return muddict
            
        
        
        
#@nonl
#@-node:234.20061005203939.2:parsemain
#@-node:234.20061005195839:class mudparse
#@-others
#@nonl
#@-node:234.20061005194826:@thin .\\Lib\\mudParser.py
#@-leo
