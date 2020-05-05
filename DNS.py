from Socket import *
from IP import *
from Packet import *
from Port import *

DNSList = {} #liste globale des de nom <-> IP
PeerList = {}

class DNS:
    def resolveName(name):
        if name in DNSList.keys():
            return DNSList[name] #renvoie une adresse IP
        else:
            return None

    def resolveIP(ip):
        if ip in PeerList.keys():
            return PeerList[ip] #Renvoie une ref au peer d'adresse demandée
        else:
            return None
