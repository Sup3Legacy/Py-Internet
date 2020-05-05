from threading import Thread
from Socket import *
from IP import *
from Packet import *
from Port import *
from DNS import *
import time

TickDelay = 0.1 #Delay between each socket-checking cycle



class Peer:
    def __init__(self, id, name = "Default", online = False, adress = IP(name = "127.0.0.0")):
        self.id = id
        PeerList[adress.name] = self
        DNSList[name] = adress
        self.name = name
        self.online = online
        self.sockets = {}
        self.receivedPackets = {} #Paquets reçus, archivés
        self.pendingData = [] #Paquets à envoyer, en attente, fournis par le client local
        self.contacts = {} #Tableau correspondance IP-socket pour ce peer (self)
        self.IPadress = adress
        self.availableSockets = []
        self.start()

    def start(self): #Démarrage
        self.thread = Thread(target = self.run)
        self.thread.start()

    def run(self): #Boucle routine
        global TickDelay
        while self.online:
            for socketId in self.sockets:
                socket = self.sockets[socketId]
                if socket.activated:
                    self.treatSocket(socket)
            if len(self.pendingData) != 0:
                for p in self.pendingData:
                    (s, d) = p
                    self.sendData(s, d)
            self.pendingData = []
            time.sleep(TickDelay)
        self.thread.stop()

    def treatSocket(self, socket): #Traite un socket s'il est activé
        self.addReceivedPackets(socket.pendingPackets)
        socket.flushPackets()
        socket.activated = False

    def createSocket(self, port): #pOuvre un port
        socket = Socket(self.IPadress, Port(name = port))
        self.sockets[port] = socket
        self.availableSockets.append(socket)

    def askSocket(self, name): #Demande un socket de réception à name (résolu avant)
        if isinstance(name, IP):
            socket = DNS.resolveIP(name.name).giveSocket(self)
            if socket != None:
                return socket
            else:
                return None
        else:
            IPadd = DNS.resolveName(name)
            if IPadd == None:
                print("Could not resolve peer name.")
                return False
            else:
                return self.askSocket(IPadd)

    def giveSocket(self, peer): #Donne un socket de réception à peer
        if peer.IPadress.name in self.contacts.keys(): #Si un socket est déjà réservé à peer
            return self.contacts[peer.IPadress.name]
        if len(self.availableSockets) == 0: #Sinon
            print("No available sockets at " + self.name + " for " + peer.name)
            return None
        else:
            socket = self.availableSockets[0]
            self.availableSockets.pop(0)
            self.contacts[peer.IPadress.name] = socket
            return socket

    def openSocket(self, port): #Met un port sur ouvert
        if port.name in self.sockets:
            self.sockets[port.name].open = True
        else:
            Print("Could not find port " + port.name)

    def sendPacket(self, packet, timeToLive = TIMETOLIVE): #private
        packet.timeToLive = timeToLive
        receiverSocket = packet.receiverSocket
        receiverSocket.activate(packet)

    def sendData(self, name, data, timeToLive = TIMETOLIVE): #public
        IPadd = DNS.resolveName(name)
        if IPadd == None:
            print("Could not resolve peer name.")
            return False
        else:
            socket = self.askSocket(name)
            if socket == None:
                print("Could not find socket in receiver peer. Should ask them to open it.")
                return False
            else:
                packet = Packet(sender = self, receiverSocket = socket, data = data)
                self.sendPacket(packet, timeToLive = TIMETOLIVE)

    def addDataToSend(self, name, data):
        self.pendingData.append((name, data))

    def addReceivedPackets(self, packets):
        self.receivedPackets.update(packets.copy())
