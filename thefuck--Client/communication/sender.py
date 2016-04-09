from socket import *
from .receiver import Receiver

class Sender():
    server_IP = 246.162.52.23
    server_Port = 9001

    def sendCommand(toBeCorrected):
        clientSocket = socket(AF_INT, SOCK_STREAM)
        clientSocket.connect((server_IP, serverPort))
        clientSocket.send(toBeCorrected)
        Receiver.receive_from_server()


