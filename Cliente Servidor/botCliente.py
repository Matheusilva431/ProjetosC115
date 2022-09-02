from socket import *
serverName = 'localhost'
serverProt = 3000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverProt))
msgcli = "init"
clientSocket.send(msgcli.encode())
while True:
    msgserve = clientSocket.recv(1024).decode()
    msgcli = input(msgserve)
    clientSocket.send(msgcli.encode())
    if msgcli == "5":
        clientSocket.close()
        break    