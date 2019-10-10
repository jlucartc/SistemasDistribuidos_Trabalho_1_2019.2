# -*- coding:utf-8 -*-

from Dispositivo import Dispositivo
from threading import Thread, get_ident, Timer
from DispReceiveUDP import DispReceiveUDP
from SendUDP import SendUDP
import Msgs_pb2
from random import *

class SensorBatimentosCardiacos(Dispositivo,Thread):

    def __init__(self,disp_host,disp_port,server_host,server_port,dict,nome):
        Dispositivo.__init__(self,dict,nome)
        Thread.__init__(self)
        self.disp_host = disp_host
        self.disp_port = disp_port
        self.server_host = server_host
        self.server_port = server_port
        ops = {
            'ler_batimentos' : str(randint(50,100))+' bpm'
        }
        self.addDictOp(ops)

    def envioContinuo(self):
        print(self.nome+" enviando dados...")
        snd = SendUDP(self.server_host,self.server_port)
        msg = Msgs_pb2.MsgSrvDisp()
        msg.tipo = Msgs_pb2.MsgSrvDisp.Tipo.RESPOSTA
        # Insira nome da operação contínua
        opnome = "ler_batimentos"
        msg.disp_id = self.id
        msg.nome_op = opnome
        snd.send(msg.SerializeToString())
        t = Timer(0.5,self.envioContinuo)
        t.start()

    def anunciar(self):
        print("Anunciando "+self.nome+"...")
        snd = SendUDP(self.server_host,self.server_port)
        msg = Msgs_pb2.MsgSrvDisp()
        msg.tipo = Msgs_pb2.MsgSrvDisp.Tipo.ANUNCIO
        disp = Msgs_pb2.Disp()
        disp.id = self.id
        disp.nome = self.nome
        disp.ops.extend(self.getOps())
        msg.disp.CopyFrom(disp)
        snd.send(msg.SerializeToString())

    def run(self):
        print("Iniciando dispositivo "+self.nome+" ...")
        self.id = str(get_ident())
        self.udp_receiver = DispReceiveUDP(self.disp_host,self.disp_port,self.server_host,self.server_port,self.id,self.getDict(),self.nome,True)
        self.udp_receiver.start()
        self.anunciar()
        self.envioContinuo()
