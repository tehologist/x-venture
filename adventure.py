
import lib.kfun as kfun
from lib.xmlworld import *

kfun.set_starting_id()
aplayer = kfun.login_player()
kfun.moveto(aplayer, 1)

while 1:
    plinput = raw_input("> ")
    kfun.cmd_parse(aplayer, plinput)
    
