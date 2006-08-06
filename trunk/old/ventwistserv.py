from twisted.protocols import basic

import lib.kfun
from lib.xmlworld import *

lib.kfun.set_starting_id()

class person:
    def __init__(self):
        self.handler = 0
        self.conn = 0
        self.name = 0
        self.id = 0
    
    def login(self, name=None):
        if self.handler != "login":
            self.conn.message("What is your name?\r")
            self.handler = "login"
        else:
            self.name = str(name)
            self.conn.message("Welcome %s\r" % (self.name))
            aplayer = lib.kfun.create_player(self.name, "A person")
            self.id = aplayer.id
            lib.kfun.moveto(aplayer, 1)
            self.handler = ""

class telmud(basic.LineReceiver):
    def connectionMade(self):
        print "Got new client."
        self.factory.clients.append(self)
        someone = person()
        someone.conn = self
        lib.kfun.people.append(someone)
        someone.login()
        
        
    def connectionLost(self, reason):
        print "Lost a client."
        self.factory.clients.remove(self)
        
    def lineReceived(self, line):
        if line:
            for pers in lib.kfun.people:
                if pers.conn == self:
                    if pers.handler == "login":
                        pers.login(line)
                    else:
                        lib.kfun.inbuffer.append((pers.id, str(line)))
                        lib.kfun.get_input()
        
            
    def message(self, message):
        self.transport.write(message + '\n')
        
from twisted.internet import protocol
from twisted.application import service, internet
from twisted.internet import task, reactor

def timepassed():
    for a in kfun.people:
        a.conn.message("Five seconds has passed.\r")

#l = task.LoopingCall(timepassed)
#l.start(5.0)

factory = protocol.ServerFactory()
factory.protocol = telmud
factory.clients = []

application = service.Application("MudServer")
internet.TCPServer(8888, factory).setServiceParent(application)

