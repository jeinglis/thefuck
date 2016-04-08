from socket import *
from .serverFacade import ServerFacade

class Reciever():

def receive_from_server():

    corrected = clientSocket.recv(1024)
    returnCorrected(corrected)
    clientSocket.close()

def return_corrected(corrected):

    ServerFacade.receive_corrected(corrected)