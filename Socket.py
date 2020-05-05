from IP import *
from Packet import *
from Port import *
from DNS import *

class Socket:
    def __init__(self, IP, Port, open = True):
        self.IPadress = IP
        self.port = Port
        self.open = open
        self.activated = False #Peding packets or not?
        self.pendingPackets = {} #Packet en attente

    def flushPackets(self):
        self.pendingPackets = {}

    def __repr__(self):
        return "Socket " + self.IPadress.name + ":" + str(self.port.name)

    def activate(self, packet):
        self.activated = True
        self.pendingPackets[packet.id] = packet
