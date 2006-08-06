from xml.dom import minidom
"""This is parser, which parses XML room files and returns data to create classes
for use within the mud."""
class room_xml_parse:
    def __init__(self, dom):
        self.name = ""
        self.id = 0
        self.description = ""
        self.exits = {}
        self.cls_obj = ""
        self.attributes = {}
        self.dom = minidom.parse(dom)
        
    def get_name(self):
        self.name = self.dom.getElementsByTagName("name")\
        [0].childNodes[0].data
        
    def get_id(self):
        var = self.dom.getElementsByTagName("id")[0]\
        .childNodes[0].data
        self.id = int(var)
        
    def get_description(self):
        var = self.dom.getElementsByTagName("description")[0]\
        .childNodes[0].data
        self.description = var

        
    def get_class(self):
        var = self.dom.getElementsByTagName("class")[0]\
        .childNodes[0].data
        self.cls_obj = var
        
    def get_exits(self):
        var = self.dom.getElementsByTagName("portals")[0]
        var = var.getElementsByTagName("name")
        var2 = {}
        for elements in var:
            for items in elements.childNodes:
                if items.nodeType == items.TEXT_NODE:
                    var = str(items.data)
                else:
                    var2[var] = int(items.childNodes[0].data)
        self.exits = var2
        
    def get_attributes(self):
        try:
            var = self.dom.getElementsByTagName("attributes")[0]
        except IndexError:
            return 0
        var = var.getElementsByTagName("label")
        var2 = {}
        for elements in var:
            for items in elements.childNodes:
                if items.nodeType == items.TEXT_NODE:
                    var = str(items.data)
                else:
                    type = items.attributes["type"].value
                    if type == "int":
                        var2[var] = int(items.childNodes[0].data)
                    if type == "string":
                        var2[var] = str(items.childNodes[0].data)
        self.attributes = var2
        
    def set_all_data(self):
        self.get_name()
        self.get_id()
        self.get_description()
        self.get_class()
        self.get_exits()
        self.get_attributes()
    
    #simple test to verify working so far    
    if __name__ == '__main__':
        from xmlroom import room_xml_parse
        thisroom = './data/rooms/room.xml'
        test = room_xml_parse(thisroom)
        test.set_all_data()
        print "Name: %s\nID: %i\nDescription: %s\nClass: %s\nExits: %s\nAttributes: %s" %\
         (test.name, test.id, test.description, test.cls_obj, test.exits, test.attributes)
        