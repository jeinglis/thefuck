from socket import *
from .clientFacade import receiveCommand

serverPort - 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print 'The Server is ready to receiver'
while 1:
        connectionSocket, addr = serverSocket.accept()
        command - connectionSocket.recv(1024)
        receiveCommand(command, connectionSocket)
        connectionSocket.close()