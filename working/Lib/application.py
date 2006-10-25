#@+leo-ver=4-thin
#@+node:234.20061024181033:@thin .\\Lib\\application.py
#@<< docstring >>
#@+middle:234.20061024181033.1:headers_footers
#@+node:234.20061024181033.2:<< docstring >>
"""A base class for deriving new applications."""
#@nonl
#@-node:234.20061024181033.2:<< docstring >>
#@-middle:234.20061024181033.1:headers_footers
#@nl
#@@language python
#@@tabwidth -4
#@<< imports >>
#@+middle:234.20061024181033.1:headers_footers
#@+node:234.20061024181033.3:<< imports >>
#@-node:234.20061024181033.3:<< imports >>
#@-middle:234.20061024181033.1:headers_footers
#@nl
#@+others
#@+node:234.20061024181033.1:headers_footers
#@-node:234.20061024181033.1:headers_footers
#@+node:234.20061024181033.4:class application
class application:
    """Base class from which all applications are derived."""
#@nonl
#@+node:234.20061024184241:__init__
    def __init__(self):
        """Setup variables to be used when class is instantiated."""
        
        self.client_list = []
        
#@nonl
#@-node:234.20061024184241:__init__
#@+node:234.20061024184947:do_handleclient
    def do_handleclient(self, client_id):
        """Check list of clients to see if person is registered. If so return True, else False."""
        
        if client_id in self.client_list:
            return True
        else:
            return False
        
        
#@nonl
#@-node:234.20061024184947:do_handleclient
#@+node:234.20061024202544:register_handler
    def register_handler(self):
        """Returns type of clients application handles."""
        
        pass
#@nonl
#@-node:234.20061024202544:register_handler
#@+node:234.20061024185326:register_client
    def register_client(self, client_id):
        self.client_list.append(client_id)
#@nonl
#@-node:234.20061024185326:register_client
#@+node:234.20061024185326.1:unregister_client
    def unregister_client(self, client_id):
        self.client_list.remove(client_id)
#@nonl
#@-node:234.20061024185326.1:unregister_client
#@+node:234.20061024185416:runapp
    def runapp(self):
        """Do some stuff."""
        pass
#@nonl
#@-node:234.20061024185416:runapp
#@-node:234.20061024181033.4:class application
#@-others
#@nonl
#@-node:234.20061024181033:@thin .\\Lib\\application.py
#@-leo
