# -*- coding:utf-8 -*-

import socket

class SendTCP:

    def __init__(self,host,port,msg):
        self.host = host
        self.port = port
        self.msg = msg
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def send(self):
        try:
            self.socket.connect((self.host,self.port))
            self.socket.send(self.msg)
            data = self.socket.recv(4096)
            print(data.decode())
        except InterruptedError:
            print("Conexão interrompida")
