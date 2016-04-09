from socket import *

class ServerSender():
    def sendToClient(connectionSocket, correctedCommands):
        connectionSocket.send(len(correctedCommands))
        for items in correctedCommands
          connectionSocket.send(items)
        connectionSocket.close()
    