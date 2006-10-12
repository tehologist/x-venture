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
        self.sentstruct = {"verb": None, "directprep": None, "directnoun": None, "indirectprep": None, "indirectnoun": None}
        self.preposition = ["IN","ON","AT"]
        
#@nonl
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
        pass
#@nonl
#@-node:234.20061005203939.1:getnoun
#@+node:234.20061005203939.2:parsemain
    def parsemain(self, cmd):
        """Calls functions in order and assigns elements to dict based on return."""
        pass
#@nonl
#@-node:234.20061005203939.2:parsemain
#@-node:234.20061005195839:class mudparse
#@-others
#@nonl
#@-node:234.20061005194826:@thin .\\Lib\\mudParser.py
#@-leo
