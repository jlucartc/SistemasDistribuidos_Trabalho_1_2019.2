# -*- coding:utf-8 -*-

# Esse é o arquivo responsável pela lógica de criação dos dispositivos.
# Para adicionar novos dispositivos, ou remover dispositivos, altere a lista
# que contém as classes de dispositivos sendo criados.

from SensorUmidade import SensorUmidade

def gerarDispositivos(disp_host,disp_port,server_host,server_port):

    lista = [SensorUmidade(disp_host,disp_port,server_host,server_port,{},"Sensor_Umidade_1")]

    for i in range(0,len(lista)):
        lista[i].start()
