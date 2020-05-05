from Socket import *
from IP import *
from Port import *
from DNS import *

TIMETOLIVE = 5 #seconds

PACKETID = 0

class Packet:
    def __init__(self, sender, receiverSocket, data, endOfLine = False, timeToLive = TIMETOLIVE):
        global PACKETID
        self.id = PACKETID
        PACKETID += 1
        self.sender = sender
        self.receiverSocket = receiverSocket
        self.data = data
        self.endOfLine = endOfLine
        self.timeToLive = timeToLive
