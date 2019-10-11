# SistemasDistribuidos_Trabalho_1_2019.2
Trabalho da cadeira de Sistemas Distribuidos

O sistema consiste em três partes: Servidor, Cliente e Dispositivos.

O servidor e os dispositivos foram feitos em Python, enquanto o cliente foi feito em Javascript, rodando no Node.js

## Instalação no Ubuntu

### Servidor 

Para rodar o servidor, vá até `<projeto>/src/Servidor` e execute o comando `python3 iniciar.py`
   
### Cliente

Para rodar o cliente, vá até `<projeto>/src/Cliente` e execute o comando `node .`. Por padrão, o servidor web iniciado        disponibilizará a aplicação no endereço `localhost:8888`. Para acessar o cliente, basta digitar `localhost:8888` na barra do navegador.

## Instalação no Windows

No windows, basta instalar o node.js baixando seu instalador em https://nodejs.org/en/download/ e executar o mesmo comando de inicialização do Cliente no cmd. O mesmo se aplica à instalação do Python, disponível em https://www.python.org/downloads/ , e à execução do Servidor.

## Sobre as mensagens

Os arquivos `.proto` que descrevem as mensagens trocadas entre as partes da aplicação estão descritos em `<projeto>/src/Mensagens/Msgs.proto`. Foi utilizada a versão 3 do Protocol Buffers.
