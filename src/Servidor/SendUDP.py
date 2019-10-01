# -*- coding:utf-8 -*-

# Interface do servidor, responsável por mandar e receber chamadas assíncronas(UDP)
# via socket.

import socket
import struct

class SendUDP:

    def __init__(self,host = "224.0.0.1", port = 9999):
        self.host = host
        self.port = port
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        except:
            print("Falha na criação do socket")

    def send(self):
        while 1:
            msg = input("Digite a mensagem: ")
            ttl = struct.pack('b', 1)
            self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
            self.socket.sendto(msg.encode(),("224.0.0.2",9998))
