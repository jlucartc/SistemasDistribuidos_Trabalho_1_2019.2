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
            #f = open("tcp_logfile_"+str(get_ident())+".txt",'a')
            #f.write(data.decode())
            data = data.decode()
            try:
                if(data == "DESCOBERTA"):
                    self.conn.send("5".encode())
                elif(data == "DADOS"):
                    self.conn.send("45 graus Celsius".encode())
                else:
                    self.conn.send(self.msg.encode())
                print("Mensagem recebida")
            except InterruptedError :
                print("Conexão interrompida")
        except PermissionError:
            print("Erro: permissão de acesso ao arquivo negada")

        self.conn.close()

    def run(self):

        self.handleMsg()
