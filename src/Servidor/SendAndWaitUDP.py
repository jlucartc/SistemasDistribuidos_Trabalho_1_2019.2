# -*- coding:utf-8 -*-

# Interface do servidor, responsável por mandar e receber chamadas assíncronas(UDP)
# via socket.

import socket
import struct
import datetime
from SendUDP import SendUDP
from threading import Thread, get_ident, Timer
import sys
import Msgs_pb2

class SendAndWaitUDP(Thread):

    def __init__(self,disp_host,disp_port,server_host,server_port,msg):
        Thread.__init__(self)
        self.disp_host = disp_host
        self.disp_port = disp_port
        self.server_host = server_host
        self.server_port = server_port
        self.msg = msg
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)

    def receive(self,rementente,destinatario):
        print("Send and wait...")
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            #if(self.listen_all == True):
            #    self.socket.bind(('',self.port))
            #else:
            self.socket.bind((self.server_host,self.server_port))
        except OSError:
            print("Erro na criação do socket. Verifique se a porta "+str(self.port)+" já está sendo utilizada")
        try:
            group = socket.inet_aton(self.disp_host)
            mreq = struct.pack("4sl",group,socket.INADDR_ANY)
            self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        except OSError:
            print("Endereço de host inválido. Verifique se o formato está correto")
            sys.exit()

        ret = None
        snd = SendUDP(self.disp_host,self.disp_port)
        while 1:
            try:
                #snd.send(self.msg)
                t1 = Timer(0.05,snd.send,[self.msg])
                t1.start()
                msg, addr = self.socket.recvfrom(1024)
            except InterruptedError:
                print("Execução interrompida")
            else:
                try:
                    ret = Msgs_pb2.MsgSrvDisp()
                    ret.ParseFromString(msg)
                    if( ret.tipo == Msgs_pb2.MsgSrvDisp.Tipo.RESPOSTA ):
                        print(str(ret.tipo))
                        break
                    print("Send and Receive - Mensagem recebida em "+str(datetime.datetime.now()))
                except PermissionError:
                    print("Erro: permissão de acesso ao arquivo negada")
        print("Saindo de Send and Wait...")
        return ret


    def run(self):

        self.receive()
