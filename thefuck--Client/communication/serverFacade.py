from .sender import Sender

class ServerFacade:

    def send_to_server(toBeCorrected):
        Sender.sendCommand(toBeCorrected)

    def receive_corrected(corrected):
        return corrected

