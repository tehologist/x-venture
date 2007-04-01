from twisted.internet import reactor, protocol
from twisted.protocols import basic
from World.Lib.telcodes import RED, NEWLINE, BLUE, RESET
import dircache, md5
import World
from World import WORLD

NOSTATE = 0
LOGIN = 1
PASSWORD = 2
NEWLOGIN = 3
NEWPASSWORD = 4
GAME = 5

INTRO = open("./Text/Intro.txt", "r").read()

class MudServer(basic.LineReceiver):
    def __init__(self):
        self.state = LOGIN
        self.username = ""
        self.loggedin = False
        self.level = 0
    def lineReceived(self, line):
        if self.state != GAME:
            self.login(line)
    def connectionMade(self):
        self.transport.write(RED + INTRO + NEWLINE)
        self.transport.write(BLUE + "Username: " + RESET)

    def login(self, line):
        if self.state == LOGIN:
            if line in dircache.listdir('./Players'):
                self.username = line
                if open("./Players/" + self.username, "r").readlines()[1].split(":")[1].isspace():
                    self.transport.write(BLUE + "Please enter a new password" + NEWLINE)
                    self.state = NEWPASSWORD
                else:
                    self.state = PASSWORD
                    self.transport.write(BLUE + "password: " + RESET)
            else:
                self.transport.write(NEWLINE + "Invalid username" + NEWLINE)
                self.transport.write(BLUE + "\r\nUsername: " + RESET)
        elif self.state == PASSWORD:
            dig = md5.new()
            dig.update(line)
            password = dig.digest()
            if password in open('./Players/' + self.username, 'r').readlines()[1].split(":")[1]:
                self.state = GAME
                WORLD.login(self)
            else:
                self.transport.write(RED + "Invalid password" + NEWLINE)
                self.transport.write(BLUE + "password: " + RESET)

        elif self.state == NEWPASSWORD:
            dig = md5.new()
            dig.update(line)
            password = dig.digest()
            page = open("./Players/" + self.username, "r").readlines()
            tmp = page[1].split(":")
            tmp[1] = password + "\n"
            page[1] = tmp[0] + ":" + tmp[1]
            page = page[0] + page[1] + page[2]
            open("./Players/" + self.username, "w+t").write(page)
            self.state = GAME
            WORLD.login(self)

        elif self.state == GAME:
            self.transport.write("Entered the game loop")
            
            

class MudServerFactory(protocol.ServerFactory):
    protocol = MudServer

if __name__ =="__main__":
    port = 5777
    reactor.listenTCP(port, MudServerFactory())
    reactor.run()
