# -*- coding:utf-8 -*-

# Interface do servidor, responsável por mandar e receber chamadas síncronas(TCP)
# via socket.

import socket

class SendTCP:

    def __init__(self,host = "0.0.0.0", port = "0"):
        self.host = host
        self.port = port
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        except:
            print("Falha na criação do socket")

    def send(self):
        self.socket.bind(self.host,self.port)
