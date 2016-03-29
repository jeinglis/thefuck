from socket import *
from .receiver import Receiver

class Sender():

serverName = 'theFuckServer'
serverPort = 12000

def connect_to_server():

    clientSocket = socket(AF_INT, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    toBeCorrected = raw_input('input goes here')
    clientSocket.send(toBeCorrected)
    Receiver.receive_from_server()



