# -*- coding:utf-8 -*-

import socket
from threading import Thread
from TCPHandler import TCPHandler

class ServerReceiveTCP(Thread):

    def __init__(self,server_tcp_host,server_tcp_port,server_udp_host,server_udp_port,disp_host,disp_port,server_id,lista):
        Thread.__init__(self)
        self.server_tcp_host = server_tcp_host
        self.server_tcp_port = server_tcp_port
        self.server_udp_host = server_udp_host
        self.server_udp_port = server_udp_port
        self.disp_host = disp_host
        self.disp_port = disp_port
        self.server_id = server_id
        self.lista = lista
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def receive(self):
        print("Aguardando conexões...")
        try:
            self.socket.bind((self.server_tcp_host,self.server_tcp_port))
            self.socket.listen()
        except OSError:
            print("Erro na criação do socket. Verifique se a porta "+str(self.server_tcp_port)+" já está sendo utilizada")
        while True:
            try:
                conn, addr = self.socket.accept()
                handler = TCPHandler(self.disp_host,self.disp_port,self.server_udp_host,self.server_udp_port,conn,self.server_id,self.lista)
                handler.start()
                print("Tratando requisição...")
            except InterruptedError :
                pritn("Conexão interrompida")

    def run(self):
        self.receive()
