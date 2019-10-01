# -*- coding:utf-8 -*-

# Interface do servidor, responsável por mandar e receber chamadas assíncronas(UDP)
# via socket.

import socket
import struct

class ReceiveUDP:

    def __init__(self,host = "224.0.0.2", port = 9998):
        self.host = host
        self.port = port
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        except:
            print("Falha na criação do socket")


    def receive(self):
        self.socket.bind((self.host,self.port))
        group = socket.inet_aton(self.host)
        mreq = struct.pack('4sL', group,socket.INADDR_ANY)
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        while 1:
            d = self.socket.recvfrom(1024)
            print("Dado recebido de "+str(d[1]))
            print("Mensagem: "+str(d[0]))
