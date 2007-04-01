"""Player class which represents in game character"""
class player:
    """Initialize name attribute"""
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj
        self.location = ""
        self.description = ""

    def do_say(self, args):
        pass

    def do_look(self, args):
        pass
