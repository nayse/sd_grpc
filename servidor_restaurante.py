from concurrent import futures
import ticket_pb2
import ticket_pb2_grpc
import grpc
import uuid

class RestauranteUniversitario(ticket_pb2_grpc.RestauranteUniversitarioServicer):

    def ComprarTicket(self, solicitacao, contexto):
        codigo_de_barras = str(uuid.uuid4()).replace('-', '')[:48]
        valor_boleto = solicitacao.valor_boleto
        resposta = ticket_pb2.CompraResposta (
            codigo_de_barras=codigo_de_barras, 
            valor_boleto=valor_boleto)
        return resposta


servidor_restaurante = grpc.server(
    futures.ThreadPoolExecutor(max_workers=5))

ticket_pb2_grpc.add_RestauranteUniversitarioServicer_to_server(
    RestauranteUniversitario(), servidor_restaurante)

servidor_restaurante.add_insecure_port('[::]:3000')

servidor_restaurante.start()
print("O servidor foi iniciado na porta: localhost:3000")

servidor_restaurante.wait_for_termination()
