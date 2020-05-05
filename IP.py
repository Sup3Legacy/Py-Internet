from Socket import *
from Packet import *
from Port import *
from DNS import *

class IP:
    def __init__(self, name = "127.0.0.0"):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name
        else:
            return False
