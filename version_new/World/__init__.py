from player import player

class world:
    def __init__(self):
        self.playerdb = {}
        self.worlddb = {}
        self.connectdb = {}
        self.currentid = 0

    def login(self, user):
        newplayer = player(user.username, self.getid())
        user.loggedin = True
        self.connectdb[user.username] = [user, newplayer]
        

    def getid(self):
        self.currentid += 1
        return self.currentid

    def playertell(playername, message):
        self.connectdb[playername][0].transport.write(message)


WORLD = world()

    
