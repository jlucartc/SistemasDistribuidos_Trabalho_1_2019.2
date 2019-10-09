# -*- coding:utf-8 -*-

# Esse é o código responsável por gerar o servidor e os dispositivos.
# para modificar a criação dos dispositivos, modifique o
# arquivo "gerarDispositivos.py".
# O módulo "definicoes" possui as constantes referentes aos endereços de
# grupos multicasts, portas e endereços TCP utilizados por servidor e dispositivos.

import definicoes as d
from Servidor import Servidor
from gerarDispositivos import gerarDispositivos

server = Servidor(d.server_udp_host,d.server_udp_port,d.server_tcp_host,d.server_tcp_port,d.disp_host,d.disp_port);

server.start()

gerarDispositivos(d.disp_host,d.disp_port,d.server_udp_host,d.server_udp_port)
