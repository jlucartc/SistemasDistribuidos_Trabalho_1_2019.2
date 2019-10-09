# -*- coding: utf-8 -*-

from threading import Thread,get_ident
import Msgs_pb2
from SendAndWaitUDP import SendAndWaitUDP
from SendUDP import SendUDP

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
            #f = open("tcp_logfile_"+str(get_ident())+".txt",'a')
            #f.write(data.decode())
            mensagem = Msgs_pb2.MsgSrvCli()
            mensagem.ParseFromString(data)
            try:
                if(mensagem.tipo == Msgs_pb2.MsgSrvCli.Tipo.DESREQ):
                    # Manda mensagem UDP multicast para grupo de dispositivos
                    snd = SendUDP(self.disp_host,self.disp_port)
                    reqmsg = Msgs_pb2.MsgSrvDisp()
                    reqmsg.tipo = Msgs_pb2.MsgSrvDisp.Tipo.DESCOBERTA
                    reqmsg.rmtt = self.server_id
                    response = Msgs_pb2.MsgSrvCli()
                    response.tipo = Msgs_pb2.MsgSrvCli.Tipo.DESRES
                    response.disps.extend(self.lista)
                    self.conn.send(response.SerializeToString())
                elif(mensagem.tipo == Msgs_pb2.MsgSrvCli.Tipo.OPREQ):
                    # Manda mensagem UDP multicast para grupo de dispositivo
                    snd = SendUDP(self.disp_host,self.disp_port)
                    reqmsg = Msgs_pb2.MsgSrvDisp()
                    reqmsg.tipo = Msgs_pb2.MsgSrvDisp.Tipo.REQUISICAO
                    reqmsg.dado = mensagem.dado
                    reqmsg.rmtt = self.server_id
                    reqmsg.dstn = mensagem.id
                    rcv = SendAndWaitUDP(self.disp_host,self.disp_port,self.server_host,self.server_port,reqmsg.SerializeToString())
                    res = rcv.receive(mensagem.id,self.server_id)
                    response = Msgs_pb2.MsgSrvCli()
                    response.tipo = Msgs_pb2.MsgSrvCli.Tipo.OPRES
                    response.id = res.rmtt
                    response.dado = mensagem.dado+"-"+res.dado
                    self.conn.send(response.SerializeToString())
            except InterruptedError :
                print("Conexão interrompida")
        except PermissionError:
            print("Erro: permissão de acesso ao arquivo negada")

        self.conn.close()

    def run(self):

        self.handleMsg()
