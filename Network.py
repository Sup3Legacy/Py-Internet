from Socket import *
from IP import *
from Packet import *
from Port import *
from Peer import *

A = Peer(0, name = "A", online = True, adress = IP(name = "125.365.245.158"))
A.createSocket(1234)

B = Peer(1, name = "B", online = True, adress = IP(name = "458.256.179.245"))
B.createSocket(0)

A.sendData("B", "Issouffle")
B.sendData("A", "LOL")

def arret():
    A.thread.stop()
    B.thread.stop()
