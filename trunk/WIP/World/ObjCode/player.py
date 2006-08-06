class player(object):

    def __init__(self, game_int):
        self.id = 0
        self.name = "nobody"
        self.description = "Some kind of loser."
        self.location = 0
        self.game_int = game_int
        self.listen = []

    def do_say(self, args):
        var = self.game_int.getObjByID(self.location)
        var.announce_others(self.id, "%s says, \"%s\"" % (self.name, args))
        self.listen.append("You say, \"%s\"" % (args))

    def do_go(self, direction):
        var = game_int.getObjByID(self.location)
        if var.Exits.has_key(direction):
            var.transport.moveTo(self.var.Exits[direction])

    
            
            

    
