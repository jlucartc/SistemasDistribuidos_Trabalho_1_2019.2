# -*- coding:utf-8 -*-

# Interface do servidor, responsável por mandar e receber chamadas assíncronas(UDP)
# via socket.

import socket
import struct
import datetime
from SendUDP import SendUDP
from threading import Thread, get_ident
import sys

class ReceiveUDP(Thread):

    def __init__(self,host = "224.0.0.0",port = 0, listen_all = False):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.listen_all = listen_all
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)

    def receive(self):
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            if(self.listen_all == True):
                self.socket.bind(('',self.port))
            else:
                self.socket.bind((self.host,self.port))
        except OSError:
            print("Erro na criação do socket. Verifique se a porta "+str(self.port)+" já está sendo utilizada")
        try:
            group = socket.inet_aton(self.host)
            mreq = struct.pack("4sl",group,socket.INADDR_ANY)
            self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        except OSError:
            print("Endereço de host inválido. Verifique se o formato está correto")
            sys.exit()

        print("Recebendo...")

        while True:
            try:
                msg, addr = self.socket.recvfrom(1024)
            except InterruptedError:
                print("Execução interrompida")
            else:
                try:
                    f = open("logfile-"+str(get_ident())+".txt",'a')
                    f.write(msg.decode()+"\n")
                    print("Mensagem recebida em "+str(datetime.datetime.now()))
                except PermissionError:
                    print("Erro: permissão de acesso ao arquivo negada")
                    
    def run(self):

        self.receive()
