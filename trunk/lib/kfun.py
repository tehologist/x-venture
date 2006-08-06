import re, sys
import objects.player as player

splitter = re.compile(' ')
db = []
ids = 0
inbuffer = []
outbuffer = []
people = []

#def send_out(id, message):
#    message = message + "\r"
#    outbuffer.append((id, message))

def send_out(id, message):
    for pers in people:
        if id == pers.id:
            pers.conn.message(message + '\r')
    
def get_players(location=0):
    varlist = []
    if location == 0:
        for pers in people:
            varlist.append(pers.id)
        return varlist
    else:
        for pers in people:
            var = find_object_by_id(pers.id)
            if var.location == location:
                varlist.append(var.id)
        return varlist
    
def announce_others(speaker, location, message):
    playerlist = get_players(location)
    for pers in playerlist:
        if pers == speaker:
            pass
        else:
            send_out(pers, message)
    
def set_starting_id():
    count = []
    global ids
    for entities in db:
        count.append(entities.id)
    count.sort()
    ids = count[len(count) - 1]
    
def register_object(anobject):
    global db
    db.append(anobject)
    
def login_player():
    name = raw_input("What is your name?")
    description = raw_input("What do you look like?")
    new_player = create_player(name, description)
    return new_player

def create_id():
    global ids
    ids = ids + 1
    return ids

def quit_game():
    print "Thank you for playing"
    sys.exit()

def moveto(anobject, location):
    anobject.location = location
    
def get_input():
    global inbuffer
    for commands in inbuffer:
        var = find_object_by_id(commands[0])
        cmd_parse(var, commands[1])
    inbuffer = []
    
def cmd_parse(pers, input):
    arg = splitter.split(input)
    doinput = "do_" + arg[0]
    if hasattr(pers, doinput):
        getattr(pers, doinput)(arg)
    elif arg[0] == "quit":
        for teh in people:
            if teh.id == pers.id:
                teh.conn.transport.loseConnection()
                db.remove(pers)
    else:
        send_out(pers.id, "No command found.")
    
def find_object_by_name(name):
    global db
    for anobject in db:
        if anobject.name.lower() == name.lower():
            break
    return anobject
    
def find_object_by_id(id):
    global db
    for anobject in db:
        if anobject.id == id:
            break
    return anobject

def find_objects_by_location(location):
    global db
    var = []
    for anobject in db:
        if hasattr(anobject, "location"):
            if anobject.location == location:
                var.append(anobject)
    return var
              

def create_player(name, description, location = None):
    pers = player.player()
    pers.name = name
    pers.description = description
    pers.location = location
    pers.id = create_id()
    print "player id %i created" % pers.id
    print pers
    register_object(pers)
    return pers

def show_objects():
    global db
    var = ""
    for anobject in db:
        var = var + "Name: %s, ID: %i, Description: %s\r" % \
        (anobject.name, anobject.id, anobject.description)
    return var

def destroy_object(anobject):
    global db
    db.remove(anobject)
    
def logout(pers):
    pass

def destroy_room(args):
    pass
    



