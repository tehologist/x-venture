"""Player class which represents in game character"""
class player:
    """Initialize name attribute"""
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.location = ""
        self.description = ""
        self.isPlayer = true

    def do_say(self, args):
        pass

    def do_look(self, args):
        pass
