from .corrector import get_corrected_commands
from .sender import sendToClient

class ClientFacade():
    def receiveCommand(command, connectionSocket):
        correctedCommands = get_corrected_commands(command)
        sendToClient(connectionSocket, correctedCommands)
