from .sender import Sender
from .corrector import 

class ServerFacade:

def send_to_server(toBeCorrected):

    Sender.connect_to_server(toBeCorrected)

def receive_corrected(corrected):

    send_corrected(corrected)

def send_corrected(corrected):

