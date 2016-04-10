from socket import *
import pickle
from .serverFacade import ServerFacade

class Reciever():
    def receive_from_server(clientSocket):
        # messageCount = 0
        # commandList = []

        # while True:
        #     if messageCount ==0:
        #         messageCount = clientSocket.recv(4)
        #   else:
        #       corrected = pickle.loads(clientSocket.recv(1024))
        #       commandList.append(corrected)
        #        if commandList.length == messageCount:
        #           returnCorrected(commandList)
        #           clientSocket.close()
        #           break

        corrected = pickle.loads(clientSocket.recv(1024))
        clientSocket.close()
        returnCorrected(corrected)

    def return_corrected(correctedList):
        ServerFacade.receive_corrected(correctedList)
