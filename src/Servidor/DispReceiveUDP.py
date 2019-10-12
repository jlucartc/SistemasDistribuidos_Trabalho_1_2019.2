# -*- coding:utf-8 -*-

import socket
import struct
import datetime
from SendUDP import SendUDP
from threading import Thread, get_ident, Timer
import Msgs_pb2
import sys
from random import *

class DispReceiveUDP(Thread):

    def __init__(self,disp_host,disp_port,server_host,server_port,id,ops,nome,is_continuo = False):
        Thread.__init__(self)
        self.disp_host = disp_host
        self.disp_port = disp_port
        self.server_host = server_host
        self.server_port = server_port
        self.id = id
        self.ops = ops
        self.nome = nome
        self.is_continuo = is_continuo
        self.disponivel = True
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)

    def configurar(self):
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

    def sumir(self):
        print("Sumindo...")
        self.disponivel = False
        t = Timer(randint(50,100)*0.5,self.aparecer)
        t.start()

    def aparecer(self):
        print("Aparecendo...")
        self.disponivel = True
        t = Timer(randint(50,100)*0.5,self.sumir)
        t.start()

    def receive(self):

        self.configurar()

        while True:
                try:
                    msg, addr = self.socket.recvfrom(1024)
                except InterruptedError:
                    print("Execução interrompida")
                else:
                    try:

                        # Desfaz a serialização da mensagem
                        ret = Msgs_pb2.MsgSrvDisp()
                        ret.ParseFromString(msg)

                        # Checa se é do tipo DESCOBERTA
                        if( ret.tipo == Msgs_pb2.MsgSrvDisp.Tipo.DESCOBERTA ):
                            if(self.disponivel == True):
                                # Constroi e envia a mensagem de resposta
                                response = Msgs_pb2.MsgSrvDisp()
                                response.tipo = Msgs_pb2.MsgSrvDisp.Tipo.DISPOSITIVO
                                disp = Msgs_pb2.Disp()
                                disp.nome = self.nome
                                disp.id = self.id
                                disp.ops.extend(self.ops)
                                response.disp.CopyFrom(disp)
                                snd = SendUDP(self.server_host,self.server_port)
                                snd.send(response.SerializeToString())
                        # Checa se é do tipo OPERACAO
                        elif( ret.tipo == Msgs_pb2.MsgSrvDisp.Tipo.OPERACAO ):
                            if( ret.disp_id == self.id ):
                                # Constroi e envia a mensagem de resposta
                                response = Msgs_pb2.MsgSrvDisp()
                                response.tipo = Msgs_pb2.MsgSrvDisp.Tipo.RESPOSTA
                                response.disp_id = ret.disp_id
                                response.nome_op = ret.nome_op
                                response.resposta = "Erro: operação inexistente"
                                if(self.disponivel == True):
                                    for i in range(0,len(self.ops.keys())):
                                        if(list(self.ops.keys())[i] == ret.nome_op):
                                            response.resposta = self.ops[list(self.ops.keys())[i]]
                                print(str(self.id)+" recebendo requisição:")
                                print("    operação: "+str(ret.nome_op))
                                print("    resultado: "+str(response.resposta))
                                snd = SendUDP(self.server_host,self.server_port)
                                snd.send(response.SerializeToString())
                    except PermissionError:
                        print("Erro: permissão de acesso ao arquivo negada")



    def run(self):
        if(self.is_continuo == False):
            t = Timer(randint(50,100)*0.5,self.sumir)
            t.start()
        self.receive()
