import grpc
import ticket_pb2
import ticket_pb2_grpc



def run():
    with grpc.insecure_channel('localhost:3000') as canal:
        conector = ticket_pb2_grpc.RestauranteUniversitarioStub(canal)
        matricula_aluno = input("Digite sua matricula: ")
        valor_boleto = float(input("Digite o valor dos Tickets a serem comprados: "))
        resposta = conector.ComprarTicket(ticket_pb2.CompraRequisicao(matricula_aluno=matricula_aluno, valor_boleto=valor_boleto))
    print("-----------------------------------------------------")
    print(f"Código de barras para pagamento: {resposta.codigo_de_barras}\n"
          f"Valor total a ser pago: R$ {resposta.valor_boleto:.2f}")
    print("-----------------------------------------------------")
if __name__ == '__main__':
    run()
