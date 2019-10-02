# -*- coding:utf-8 -*-

# Interface do servidor, responsável por mandar e receber chamadas assíncronas(UDP)
# via socket.

import socket
import struct
from threading import Thread
import sys

class ReceiveUDP(Thread):

    def __init__(self,host = "224.0.0.2",port = 9998, listen_all = False):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.listen_all = listen_all
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
        except:
            print("Falha na criação do socket")
            sys.exit()

    def receive(self):
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if(self.listen_all == True):
                self.socket.bind(('',self.port))
            else:
                self.socket.bind((self.host,self.port))
            group = socket.inet_aton(self.host)
            mreq = struct.pack("4sl",group,socket.INADDR_ANY)
            self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        except:
            print("Falha na criação do socket. Verifique se a porta "+str(self.port)+" já está sendo utilizada.")
            sys.exit()

        print("Recebendo...")

        while True:
            d = self.socket.recvfrom(1024)
            print("Receptor "+str(self.port)+"\n")
            print("     Dado recebido de "+str(d[1])+"\n")
            print("     Mensagem: "+str(d[0])+"\n")

    def run(self):

        self.receive()
