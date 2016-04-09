from socket import *
from .serverFacade import ServerFacade

class Reciever():
    def receive_from_server():
      messageCount = 0
     commandList = []

        while True:
            if messageCount ==0:
                messageCount = clientSocket.recv(1024)
          else:
              corrected = clientSocket.recv(1024)
              commandList.append(corrected)
               if commandList.length == messageCount:
                  returnCorrected(commandList)
                  clientSocket.close()
                  break

    def return_corrected(correctedList):
        ServerFacade.receive_corrected(correctedList)
