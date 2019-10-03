# -*- coding:utf-8 -*-

from ReceiveUDP import ReceiveUDP
from ReceiveTCP import ReceiveTCP

class Servidor :

    # Servidor deve ser capaz de escutar requisições de qualquer grupo através de uma mesma porta
    # Os dispositivos devem estar todos no mesmo grupo:porta, onde a porta já é conhecida pelo servidor

    def __init__(udp_host = "224.1.1.1", udp_port = 9999, tcp_host = "127.0.0.1", tcp_port = 9998):
       	self.udp_receiver = ReceiveUDP(udp_host,udp_port)
        self.tcp_receiver = ReceiveTCP(tcp_host,tcp_port)

    def start():
        self.udp_receiver.start()
        self.tcp_receiver.start()
