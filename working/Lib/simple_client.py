#@+leo-ver=4-thin
#@+node:234.20061019180722.3:@thin .\\Lib\simple_client.py
#@<< docstring >>
#@+middle:234.20061019180722.4:headers_footers
#@+node:234.20061019180722.5:<< docstring >>
"""An example of the simplest possible client."""
#@nonl
#@-node:234.20061019180722.5:<< docstring >>
#@-middle:234.20061019180722.4:headers_footers
#@nl
#@@language python
#@@tabwidth -4
#@<< imports >>
#@+middle:234.20061019180722.4:headers_footers
#@+node:234.20061019180722.6:<< imports >>
#@-node:234.20061019180722.6:<< imports >>
#@-middle:234.20061019180722.4:headers_footers
#@nl
#@+others
#@+node:234.20061019180722.4:headers_footers
#@+node:234.20061024172236:class simpleclient
class simpleclient:
    """Can receive and send basic messages."""
    
    def __init__(self):
        """IN buffer, OUT buffer, and message format."""
        
        self.IN = []
        self.OUT = []
        self.MSG = {"client_ID":"self.client","msgtype":"msg","msg":None}
        self.client = "simpleclient.1"
        
    def create_msg(self, msg, msgtype="msg"):
        """Subclass and overide this method to support others."""
        
        message = self.MSG
        message[msg] = msg
        return message
        
    def message_send(self, message):
        """Just append to OUT, in application there would be a daemon which would parse all outputs and send them."""
        
        self.OUT.append(message)
        
    def message_recieve(self):
        """A daemon also goes through client list and appends any messages for client to input."""
        
        messages = self.IN
        for message in messages:
            yield message[msg]
        
#@nonl
#@-node:234.20061024172236:class simpleclient
#@-node:234.20061019180722.4:headers_footers
#@-others
#@nonl
#@-node:234.20061019180722.3:@thin .\\Lib\simple_client.py
#@-leo
