from Socket import *
from IP import *
from Packet import *
from DNS import *

class Port:
    def __init__(self, name = 0):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return int(self.name) == int(other.name)
        else:
            return False
