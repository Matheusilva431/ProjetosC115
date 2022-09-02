from socket import *

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)
# atribui a porta ao socket criado
serverSocket.bind(("", serverPort))
# aceita conexoes
# com no maximo um cliente na fil
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()
escolha = connectionSocket.recv(1024).decode()
msgCliente = "Olá, insira o numero do telefone: "
connectionSocket.send(msgCliente.encode())
# Recebe o numero
telefone = connectionSocket.recv(1024).decode()

while True:
    
    msgCliente = f"Olá, parar o número {telefone}:\n    2 - Para fatura\n    3 - Para o saldo\n    4 - Para cancelamento\n    5 - Para encerrar a chamada\n    Sua escolha: "
    connectionSocket.send(msgCliente.encode())
    escolha = connectionSocket.recv(1024).decode()
    if escolha == "2":
        msgCliente = f"A fatura, do numero {telefone}, com vencimento em set/2022  ́e de R$220,00\n"
        connectionSocket.send(msgCliente.encode())
        continue
    elif escolha == "3":
        msgCliente = f"Você esta com 52,5 em saldo para ligações e 400mb internet no numero de telefone {telefone}\n"
        connectionSocket.send(msgCliente.encode())
        continue
    elif escolha == "4":
        msgCliente = "Para mais informações de cancelamento ligue para 0800-4965\n"
        connectionSocket.send(msgCliente.encode())
        continue
    else:
        connectionSocket.close()
        break