# gRPC Remote Procedure Call

Disciplina: Sistemas Distribuidos

Alunos: Nayse Fagundes e Gabriel Farias 

## Tema 7: Compra de ticket do Restaurante universitário

o cliente informa matricula e valor a ser pago

o servidor responde: código de barras e valor total


## Instalação


Necessário possuir Python, e as bibliotecas concurrent.futures, grpcio e grpcio-tools, e uuid instalados.


```
pip install grpcio grpcio-tools
pip install uuid
```

## Execução

Dentro do diretório com o aqrquivo ticket.proto executar:
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ticket.proto
```

Isso irá gerar os arquivos ticket_pb2 e ticket_pb2_grpc, dentro do diretório principal do arquivo dos códigos.

Em prompts de comandos diferente executar o arquivo do servidor:

```
python servidor_restaurante.py
```
EM seguida execute o arquivo que direciona ao arquive do cliente: 
```
python execute.py
```
Quando executado informar _número de matricula_ e _valor_ a ser pago pelos Tickets. O programa retornará o código de barras e o valor total.


_Documentação gRPC em python:_ https://grpc.io/docs/languages/python/basics/
