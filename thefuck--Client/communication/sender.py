from socket import *
import pickle
from .receiver import receive_from_server


SERVER_IP = 246.162.52.23
SERVER_PORT = 9001

def send_command(to_be_corrected):
    client_socket = socket(AF_INT, SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    client_socket.send(pickle.dumps(to_be_corrected))
    Receiver.receive_from_server(client_socket)


