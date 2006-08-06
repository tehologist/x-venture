from pyparsing import *

verbSay = CaselessLiteral("SAY").setResultsName("verb")
verbLook = oneOf("LOOK L", caseless=True).setParseAction(replaceWith("LOOK")).setResultsName("verb")
verbInv = oneOf("INVENTORY INV I", caseless=True).setParseAction(replaceWith("INV")).setResultsName("verb")
verbMove = oneOf("MOVE GO", caseless=True).setParseAction(replaceWith("go"))
verbTake = oneOf("TAKE GET", caseless=True).setParseAction(replaceWith("TAKE")).setResultsName("verb")
verbDrop = CaselessLiteral("DROP").setResultsName("verb")
verbQuit = CaselessLiteral("QUIT").setResultsName("verb")

verbGen = Word(alphas).setResultsName("verb")

nounObj = Combine(OneOrMore(Word(alphas) | White()))

prep = oneOf("IN ON AT AROUND UNDER FROM ABOVE BENEATH", caseless=True).setResultsName("prep")

neDir = oneOf("NE NORTHEAST", caseless=True).setParseAction(replaceWith("NE"))
nwDir = oneOf("NW NORTHWEST", caseless=True).setParseAction(replaceWith("NW"))
seDir = oneOf("SE SOUTHEAST", caseless=True).setParseAction(replaceWith("SE"))
swDir = oneOf("SW SOUTHWEST", caseless=True).setParseAction(replaceWith("SW"))
nDir = oneOf("N NORTH", caseless=True).setParseAction(replaceWith("N"))
eDir = oneOf("E EAST", caseless=True).setParseAction(replaceWith("E"))
sDir = oneOf("S SOUTH", caseless=True).setParseAction(replaceWith("S"))
wDir = oneOf("W WEST", caseless=True).setParseAction(replaceWith("W"))
upDir = CaselessLiteral("UP")
dnDir = CaselessLiteral("DOWN")
moveDirection = neDir | nwDir | seDir | swDir | upDir | dnDir | nDir | eDir | sDir | wDir  

cmdSay = verbSay + nounObj.setResultsName("args")
cmdLook = verbLook + Optional(prep) + nounObj.setResultsName("dirObj")
cmdInv = verbInv
cmdMove = verbMove.setResultsName("verb") + moveDirection.setResultsName("dir")
cmdTake = verbTake + nounObj.setResultsName("dirObj") + Optional(prep) + Optional(nounObj.setResultsName("indObj"))
cmdDrop = verbDrop + nounObj.setResultsName("dirObj")
cmdQuit = verbQuit
