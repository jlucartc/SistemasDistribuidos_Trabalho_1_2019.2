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

class DispReceiveUDP(Thread):

    def __init__(self,disp_host,disp_port,server_host,server_port,id,ops,nome):
        Thread.__init__(self)
        self.disp_host = disp_host
        self.disp_port = disp_port
        self.server_host = server_host
        self.server_port = server_port
        self.id = id
        self.ops = ops
        self.nome = nome
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)

    def receive(self):
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((self.disp_host,self.disp_port))
        except OSError:
            print("Erro na criação do socket. Verifique se a porta "+str(self.disp_port)+" já está sendo utilizada")
        try:
            group = socket.inet_aton(self.disp_host)
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
                    print("DispReceiveUDP: "+str(ret.tipo))
                    if( ret.tipo == Msgs_pb2.MsgSrvDisp.Tipo.DESCOBERTA ):
                        response = Msgs_pb2.MsgSrvDisp()
                        response.tipo = Msgs_pb2.MsgSrvDisp.Tipo.DESCOBERTA
                        response.dstn = ret.rmtt
                        response.rmtt = self.nome
                        disp = Msgs_pb2.Disp()
                        disp.nome = self.nome
                        disp.id = self.id
                        disp.ops.extend(self.ops)
                        response.disps.extend([disp])
                        snd = SendUDP(self.server_host,self.server_port)
                        print("Dispositivo "+self.nome+" enviando descoberta para servidor...")
                        snd.send(response.SerializeToString())
                    elif( ret.tipo == Msgs_pb2.MsgSrvDisp.Tipo.REQUISICAO ):
                        print("ret.dstn: "+str(ret.dstn))
                        print("self.id: "+str(self.id))
                        if( ret.dstn == self.id ):
                            response = Msgs_pb2.MsgSrvDisp()
                            response.tipo = Msgs_pb2.MsgSrvDisp.Tipo.RESPOSTA
                            response.dstn = ret.rmtt
                            response.rmtt = ret.dstn
                            print("OPS: "+str(self.ops))
                            response.dado = ""
                            for i in range(0,len(self.ops.keys())):
                                if(list(self.ops.keys())[i] == ret.dado):
                                    response.dado = self.ops[list(self.ops.keys())[i]]
                            print("Operação encontrada: "+str(response.dado))
                            snd = SendUDP(self.server_host,self.server_port)
                            print("Enviando RESPOSTA...")
                            snd.send(response.SerializeToString())
                    else:
                        print("DispReceiveUDP...")
                except PermissionError:
                    print("Erro: permissão de acesso ao arquivo negada")



    def run(self):

        self.receive()
