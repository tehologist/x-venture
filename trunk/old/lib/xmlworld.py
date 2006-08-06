import lib.xmlroom as xmlroom
import lib.xmlobjects as xmlobjects
import lib.kfun as kfun
import os
import fnmatch

def get_xml_files(files):
    var = []
    for items in files:
        if fnmatch.fnmatch(items, '*.xml'):
            var.append(items)
    return var

def init_world(rooms=None, objects=None):
    for item in rooms:
        roomdata = xmlroom.room_xml_parse('./data/rooms/'+item)
        roomdata.set_all_data()
        roombase = __import__('objects.'+roomdata.cls_obj,globals(),locals()\
        ,['room'])
        create_room(roomdata.name, roomdata.description, roomdata.id,\
        roomdata.exits, roombase)
            
    for item in objects:
        objectdata = xmlobjects.object_xml_parse('./data/things/'+item)
        objectdata.set_all_data()
        objectbase = __import__('objects.'+objectdata.cls_obj,globals(),locals()\
        ,['object'])
        create_object(objectdata.name, objectdata.description, objectdata.location,\
         objectdata.id, objectbase)

def create_object(name, description, location, id=None, baseclass=None):
    anobject = baseclass.object()
    anobject.name = name
    anobject.description = description
    anobject.location = location
    if id is None:
        anobject.id = kfun.create_id()
    else:
        anobject.id = id
    print "object id %i created" % anobject.id
    kfun.register_object(anobject)

def create_room(name, description, id = None, exits=None, baseclass=None):
    aroom = baseclass.room()
    aroom.name = name
    aroom.description = description
    aroom.exits = exits
    if id is None:
        aroom.id = kfun.create_id()
    else:
        aroom.id = id
    print "room id %i created" % aroom.id
    print aroom.exits
    kfun.register_object(aroom)

files = os.listdir('./data/rooms')
rooms = get_xml_files(files)
files = os.listdir('./data/things')
gobjects = get_xml_files(files)
init_world(rooms, gobjects)