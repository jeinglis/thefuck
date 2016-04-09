from socket import *
from .clientFacade import ClientFacade

class ServerReceiver():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    def listenForConnection():
        serverPort - 12000
        serverSocket.bind(('', serverPort))
        serverSocket.listen(1)
        print 'The Server is ready to receiver'
        while 1:
            connectionSocket, addr = serverSocket.accept()
            command - connectionSocket.recv(1024)
            sendForCorrection(command, connectionSocket)

    def sendForCorrection(command, connectionSocket):
            receiveCommand(command, connectionSocket)