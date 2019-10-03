# -*- coding: utf-8 -*-

from threading import Thread,get_ident

class TCPHandler(Thread):

    def __init__(self,conn,msg):
        Thread.__init__(self)
        self.conn = conn
        self.msg = msg

    def handleMsg(self):

        try:
            data = self.conn.recv(4096);
        except InterruptedError:
            print("Conexão interrompida")
        try:
            f = open("tcp_logfile_"+str(get_ident())+".txt",'a')
            f.write(data.decode())
            print("Mensagem recebida")
        except PermissionError:
            print("Erro: permissão de acesso ao arquivo negada")
        try:
            self.conn.send(self.msg.encode())
        except InterruptedError:
            print("Conexão interrompida")
        self.conn.close()

    def run(self):

        self.handleMsg()
