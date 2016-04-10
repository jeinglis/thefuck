from .receiver import ServerReceiver
import sys

def main():
    port = 0
    port = sys.argv[1]
    ServerReceiver.listenForConnection(port);
