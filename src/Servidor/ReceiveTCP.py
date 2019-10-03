# -*- coding:utf-8 -*-

import socket
from TCPHandler import TCPHandler

class ReceiveTCP:

    def __init__(self,host = "127.0.0.1", port = "9998", msg = "Conexão estabelecida"):
        self.host = host
        self.port = port
        self.msg = msg
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def receive(self):
        print("Aguardando conexões...")
        try:
            self.socket.bind((self.host,self.port))
            self.socket.listen()
        except OSError:
            print("Erro na criação do socket. Verifique se a porta "+str(self.port)+" já está sendo utilizada")
        while True:
            try:
                conn, addr = self.socket.accept()
                handler = TCPHandler(conn,self.msg)
                handler.start()
                print("Tratando requisição...")
            except InterruptedError :
                pritn("Conexão interrompida")
