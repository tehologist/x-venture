import lib.kfun
class player:
    def __init__(self):
        self.name = ""
        self.location = 0
        self.description = ""
        self.id = 0
        self.contains = []
    
    def do_say(self, args):
        sentence = ""
        for words in args:
            if words == "say":
                pass
            else:
                if args.index(words) + 1 == len(args):
                    sentence += words
                else:
                    sentence += words + " "
        lib.kfun.send_out(self.id, "You say, \"%s\"" % sentence)
        lib.kfun.announce_others(self.id, self.location, "%s says, \"%s\""\
         % (self.name, sentence))
        
    def do_objects(self, args):
        var = lib.kfun.show_objects()
        lib.kfun.send_out(self.id, str(var))
    
    def do_look(self, args):
        view = lib.kfun.find_object_by_id(self.location)
        lib.kfun.send_out(self.id, "%s\n" % str(view.description))
        lib.kfun.send_out(self.id, "Exits: %s\n" % view.exits.keys())
        var = []
        var = lib.kfun.find_objects_by_location(self.location)
        if len(var) >= 2:
            lib.kfun.send_out(self.id, "\nThis room contains.")
            for things in var:
                if str(things.name) != str(self.name):
                    lib.kfun.send_out(self.id, "%s\n" % str(things.name))
        
    def do_go(self, args):
        thisroom = lib.kfun.find_object_by_id(self.location)
        if thisroom.exits.has_key(args[1]):
            thatroom = thisroom.exits[args[1]]
            lib.kfun.moveto(self, thatroom)
            lib.kfun.send_out(self.id,"You go %s." % args[1])
        else:
            lib.kfun.send_out(self.id, "You cannot go that way.")
            
    def do_exits(self, args):
        thisroom = lib.kfun.find_object_by_id(self.location)
        lib.kfun.send_out(self.id, str(thisroom.exits.keys()))
        
    def do_take(self, args):
        pass
        
    def do_inventory(self, args):
        pass
    
    def do_drop(self, args):
        pass
