# -*- coding:utf-8 -*-

from ServerReceiveUDP import ServerReceiveUDP
from ServerReceiveTCP import ServerReceiveTCP
from SendUDP import SendUDP
from threading import Thread, Timer, get_ident
import Msgs_pb2
from random import *

class Servidor(Thread) :

    # Servidor deve ser capaz de escutar requisições de qualquer grupo através de uma mesma porta
    # Os dispositivos devem estar todos no mesmo grupo:porta, onde a porta já é conhecida pelo servidor

    def __init__(self,server_udp_host,server_udp_port,server_tcp_host,server_tcp_port,disp_host,disp_port):
        Thread.__init__(self)
        self.lista = []
        self.server_udp_host = server_udp_host
        self.server_udp_port = server_udp_port
        self.server_tcp_host = server_tcp_host
        self.server_tcp_port = server_tcp_port
        self.disp_host = disp_host
        self.disp_port = disp_port

    def descobrir(self):
        print("Servidor descobrindo dispositivos...")
        self.lista = []
        snd = SendUDP(self.disp_host,self.disp_port)
        msg = Msgs_pb2.MsgSrvDisp()
        msg.tipo = Msgs_pb2.MsgSrvDisp.Tipo.DESCOBERTA
        msg.rmtt = self.server_id # definir isso
        msg.dstn = self.server_id
        snd.send(msg.SerializeToString())
        t = Timer(randint(1,100)*0.5,self.descobrir)
        t.start()

    def iniciar(self):
        self.udp_receiver.start()
        self.tcp_receiver.start()
        self.descobrir()

    def run(self):
        self.server_id = str(get_ident())
        self.udp_receiver = ServerReceiveUDP(self.server_udp_host,self.server_udp_port,self.disp_host,self.disp_port,self.server_id,self.lista)
        self.tcp_receiver = ServerReceiveTCP(self.server_tcp_host,self.server_tcp_port,self.server_udp_host,self.server_udp_port,self.disp_host,self.disp_port,self.server_id,self.lista)
        self.iniciar()
