#import sys #maybe not necessary if argparse already handles all of this
import socket
import threading
import argparse

class Connection:

    def __init__(self, ):
        #buffers
        self._machine_a_in = ''
        self._machine_a_out = ''
        self._machine_b_in = ''
        self._machine_b_out = ''

    def connect_in(self):
        pass

    def connect_out(self):
        pass

    def udp_in(self):
        raise NotImplementedError

    def udp_out(self):
        raise NotImplementedError

    def main(self):
        pass

# interpret args passed to program
# localaddr, localport, remoteaddr, remoteport

arg_parser = argparse.ArgumentParser(description = "Simple 1:1 proxy - Example usage: proxy.py -p 8080 -r 192.168.0.1 -d 80")
arg_parser.add_argument('-l', '--local-addr', default = '0.0.0.0', dest = 'local_address', help = 'The local address to bind to (default: 0.0.0.0)')
arg_parser.add_argument('-p', '--local-port', required = True, dest = 'local_port', help = 'The local TCP port to bind to')
arg_parser.add_argument('-r', '--remote-addr', required = True, dest = 'remote_address', help = 'The remote address to connect to')
arg_parser.add_argument('-d', '--remote-port', required = True, dest = 'remote_port', help = 'The remote port to connect to')

args = arg_parser.parse_args()
#apparently parse_args() will just close the program here if the user asks for help (-h)

#game/connection loop

while True:
    try:
        #listen for stuff
        #when something connects, spawn a thread and try to establish the outgoing connection
        #profit
    except KeyboardInterrupt:
        #clean up please
        break # <- this is not clean >:V