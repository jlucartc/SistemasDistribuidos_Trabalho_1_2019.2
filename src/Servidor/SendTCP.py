# -*- coding:utf-8 -*-

import socket

class SendTCP:

    def __init__(self,host = "0.0.0.0", port = "0", msg = ""):
        self.host = host
        self.port = port
        self.msg = msg
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def send(self):
        try:
            self.socket.connect((self.host,self.port))
            self.socket.send(self.msg.encode())
            data = self.socket.recv(4096)
            print(data.decode())
        except InterruptedError:
            print("Conexão interrompida")
