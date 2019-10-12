# SistemasDistribuidos_Trabalho_1_2019.2
Trabalho da cadeira de Sistemas Distribuidos

O sistema consiste em três partes: Servidor, Cliente e Dispositivos.

O servidor e os dispositivos foram feitos em Python, enquanto o cliente foi feito em Javascript, rodando no Node.js

## Instalação no Ubuntu

Para rodar o sistema em uma máquina local, primeiro clone este repositório digitando o comando:

`git clone https://github.com/jlucartc/SistemasDistribuidos_Trabalho_1_2019.2.git <nome_da_pasta_de_destino>`

Caso o parâmetro `<nome_da_pasta_de_destino>` seja omitido, o projeto será criado dentro de uma pasta com o nome do repositório.

### Servidor 

Para rodar o servidor, vá até `<nome_da_pasta_de_destino>/src/Servidor` e execute o comando `python3 iniciar.py`
   
### Cliente

OBS: A versão do `node` utilizada foi a versão 11.0.0

Para rodar o cliente, vá até `<nome_da_pasta_de_destino>/src/Cliente` e execute o comando `node .` . Por padrão, o servidor web iniciado        disponibilizará a aplicação no endereço `localhost:8888`. Para acessar o cliente, basta digitar `localhost:8888` na barra do navegador.

## Instalação no Windows

No windows, basta instalar o node.js baixando seu instalador em https://nodejs.org/en/download/ e executar o mesmo comando de inicialização do Cliente no cmd. O mesmo se aplica à instalação do Python, disponível em https://www.python.org/downloads/ , e à execução do Servidor.

## Sobre as mensagens

Os arquivos `.proto` que descrevem as mensagens trocadas entre as partes da aplicação estão descritos em `<nome_da_pasta_de_destino>/src/Mensagens/Msgs.proto`. Foi utilizada a versão 3 do Protocol Buffers.

Para gerar os arquivos compilados em python, foi utilizado o comando `protoc --proto-path=. --python-out=. Msgs.proto` dentro do diretório `/home/<usuario>/<nome_da_pasta_de_destino>/src/Mensagens`. Em seguida, basta movê-los para a pasta dos `Servidor`.

Quando à parte em Javascript, não é necessário gerar os arquivos `.js`, pois a biblioteca [protocol-buffers](https://www.npmjs.com/package/protocol-buffers) abre o arquivo `Msgs.proto` e gera as mensagens em tempo de execução. Portanto, para que o Cliente utilize as mensagens, basta copiar `Msgs.proto` para a pasta `Cliente/js/`.

## Adicionando novos dispositivos

Todas as classes de dispositivos utilizados se encontram em `<nome_da_pasta_de_destino>/src/Servidor`

Para adicionar novos dispositivos, sugere-se que o código desses novos dispositivos sejam cópias de dispositivos já existentes, mudando apenas os nomes das classes e as operações realizadas.

Para dispositivos normais, como `SensorTemperatura.py` e `SensorUmidade.py`, basta copiar o código de algum destes e modificar sua variável `opt` dentro do construtor da classe. A variável `opt` consiste em um dicionário, onde a chave é o nome da operação e o valor é o valor de retorno. Esse valor de retorno é sempre o mesmo, por questão de simplicidade.

Para dispositivos que possuem algum método de envio contínuo, o modelo será a classe em `SensorBatimentosCardiacos.py`. Para esses dispositivos, as instruções do caso anterior também se aplicam, com o diferencial de que no método `envioContinuo()`, a variável `opnome` deve receber o nome da operação a ser enviada continuamente.

Após a definição da classe, para que o programa crie as instâncias, o arquivo `gerarDispositivos.py` deve ser atualizado. Primeiro, a classe do dispositivo deve ser importada através da adição da linha `from <nome_arquivo> import <nome_classe>`. Em seguida, uma instância da classe deve ser adicionada à lista dentro de `gerarDispositivos()`, de forma que apenas o último parâmetro, que é o nome do dispositivo, poderá ser customizado. O nome serve para que o usuário possa diferenciar os dispositivos. Dispositivos de mesmo nome não irão entrar em conflito por conta disso.
