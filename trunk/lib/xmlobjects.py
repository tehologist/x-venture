from xml.dom import minidom
"""This is parser, which parses XML object files and returns data to create classes
for use within the mud."""
class object_xml_parse:
    def __init__(self, dom):
        self.name = ""
        self.id = 0
        self.description = ""
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
        
    def get_location(self):
        var = self.dom.getElementsByTagName("location")[0]\
        .childNodes[0].data
        self.location = int(var)
        
    def set_all_data(self):
        self.get_name()
        self.get_id()
        self.get_description()
        self.get_class()
        self.get_location()
        self.get_attributes()
        
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
    
    #simple test to verify working so far    
    if __name__ == '__main__':
        from xmlobjects import object_xml_parse
        thisthing = './data/things/cane.xml'
        test = object_xml_parse(thisthing)
        test.set_all_data()
        print "Name: %s\nID: %i\nDescription: %s\nClass: %s\nLocation:\
        %s\nAttributes: %s" % (test.name, test.id, test.description, test.cls_obj\
        , test.location, test.attributes)