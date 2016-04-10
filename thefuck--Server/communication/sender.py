from socket import *
import pickle

class ServerSender():
    def sendToClient(connectionSocket, correctedCommands):
        # connectionSocket.send(str(len(correctedCommands)))
        # for items in correctedCommands:
        #     connectionSocket.send(pickle.dumps(items))
        connectionSocket.send(pickle.dumps(correctedCommands))
        connectionSocket.close()
    