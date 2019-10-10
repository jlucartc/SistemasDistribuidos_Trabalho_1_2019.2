# -*- coding: utf-8 -*-

from threading import Thread,get_ident
import Msgs_pb2
from SendAndWaitUDP import SendAndWaitUDP
from SendUDP import SendUDP
import socket

class TCPHandler(Thread):

    def __init__(self,disp_host,disp_port,server_host,server_port,conn,server_id,lista):
        Thread.__init__(self)
        self.conn = conn
        self.disp_host = disp_host
        self.disp_port = disp_port
        self.server_host = server_host
        self.server_port = server_port
        self.server_id = server_id
        self.lista = lista

    def handleMsg(self):

        try:
            data = self.conn.recv(4096);
        except InterruptedError:
            print("Conexão interrompida")
        try:
            mensagem = Msgs_pb2.MsgSrvCli()
            mensagem.ParseFromString(data)
            try:
                if(mensagem.tipo == Msgs_pb2.MsgSrvCli.Tipo.DESCOBERTA):
                    # Manda mensagem UDP multicast para grupo de dispositivos
                    response = Msgs_pb2.MsgSrvCli()
                    print("Lista do servidor: "+str(self.lista))
                    response.tipo = Msgs_pb2.MsgSrvCli.Tipo.DISPOSITIVOS
                    response.disps.extend(self.lista)
                    self.conn.send(response.SerializeToString())
                elif(mensagem.tipo == Msgs_pb2.MsgSrvCli.Tipo.OPERACAO):
                    # Manda mensagem UDP multicast para grupo de dispositivo
                    reqmsg = Msgs_pb2.MsgSrvDisp()
                    reqmsg.tipo = Msgs_pb2.MsgSrvDisp.Tipo.OPERACAO
                    reqmsg.disp_id = mensagem.disp_id
                    reqmsg.nome_op = mensagem.nome_op
                    rcv = SendAndWaitUDP(self.disp_host,self.disp_port,self.server_host,self.server_port,reqmsg)
                    res = rcv.receive()
                    response = Msgs_pb2.MsgSrvCli()
                    response.tipo = Msgs_pb2.MsgSrvCli.Tipo.RESPOSTA
                    response.disp_id = res.disp_id
                    response.resposta = res.resposta
                    self.conn.send(response.SerializeToString())
            except InterruptedError :
                print("Conexão interrompida")
        except PermissionError:
            print("Erro: permissão de acesso ao arquivo negada")

        self.conn.close()

    def run(self):

        self.handleMsg()
