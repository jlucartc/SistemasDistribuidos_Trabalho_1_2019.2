# -*- coding:utf-8 -*-

# Interface do servidor, responsável por mandar e receber chamadas assíncronas(UDP)
# via socket.

import socket
import struct
from threading import Thread
import sys

class SendUDP:

    def __init__(self,host,port):
        #super().__init__()
        self.host = host
        self.port = port
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        except:
            print("Falha na criação do socket")
            sys.exit()

    def send(self,msg):
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
        self.socket.sendto(msg,(self.host,self.port))
