from socket import *
from .receiver import Receiver

class Sender():
    serverName = 'theFuckServer'
    serverPort = 9001

    def sendCommand(toBeCorrected):
         clientSocket = socket(AF_INT, SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))
        clientSocket.send(toBeCorrected)
        Receiver.receive_from_server()




