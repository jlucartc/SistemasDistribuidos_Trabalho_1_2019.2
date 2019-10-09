# -*- coding:utf-8 -*-

# Interface do servidor, responsável por mandar e receber chamadas assíncronas(UDP)
# via socket.

import socket
import struct
import datetime
from SendUDP import SendUDP
from threading import Thread, get_ident
import Msgs_pb2
import sys

class ServerReceiveUDP(Thread):

    def __init__(self,server_host,server_port,disp_host,disp_port,server_id,lista):
        Thread.__init__(self)
        self.server_host = server_host
        self.server_port = server_port
        self.disp_host = disp_host
        self.disp_port = disp_port
        self.lista = lista
        self.server_id = server_id
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)

    def receive(self):
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.server_host,self.server_port))
        except OSError:
            print("Erro na criação do socket. Verifique se a porta "+str(self.server_port)+" já está sendo utilizada")
        try:
            group = socket.inet_aton(self.server_host)
            mreq = struct.pack("4sl",group,socket.INADDR_ANY)
            self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        except OSError:
            print("Endereço de host inválido. Verifique se o formato está correto")
            sys.exit()

        while True:
            try:
                msg, addr = self.socket.recvfrom(1024)
            except InterruptedError:
                print("Execução interrompida")
            else:
                try:
                    ret = Msgs_pb2.MsgSrvDisp()
                    ret.ParseFromString(msg)
                    if( ret.tipo == Msgs_pb2.MsgSrvDisp.Tipo.ANUNCIO ):
                        for i in range(0,len(ret.disps)):
                            self.lista.append(ret.disps[i])
                            print("Servidor "+self.server_id+" recebendo anuncio de "+ret.disps[i].nome+" em "+str(datetime.datetime.now()))
                    elif( ret.tipo == Msgs_pb2.MsgSrvDisp.Tipo.DESCOBERTA ):
                        if( ret.dstn == self.server_id ):
                            print("Servidor recebendo descoberta de "+ret.rmtt)
                            for i in range(0,len(ret.disps)):
                                c = False
                                for j in range(0,len(self.lista)):
                                    if( self.lista[j].id == ret.disps[i].id ):
                                        c = True
                                        break
                                if(c == False):
                                    self.lista.append(ret.disps[i])
                    elif( ret.tipo == Msgs_pb2.MsgSrvDisp.Tipo.RESPOSTA ):
                        if( ret.dstn == self.server_id ):
                            print("Mensagem recebida em "+str(datetime.datetime.now()))
                            print("Dado: "+str(ret.dado))
                except PermissionError:
                    print("Erro: permissão de acesso ao arquivo negada")



    def run(self):

        self.receive()
