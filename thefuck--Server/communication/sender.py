from socket import *

class ServerSender():
    
def sendToClient(connectionSocket, correctedList):
    connectionSocket.send(len(correctedList))
    for items in correctedList
        connectionSocket.send(items)
    connectionSocket.close()
    