#import sys #maybe not necessary if argparse already handles all of this
import socket
import threading
import argparse

class Connection:

    def __init__(self, incoming_socket, outgoing_addr, outgoing_port,
                 **kwargs):
        #buffers
        self._machine_a_in = ''
        self._machine_a_out = ''
        self._machine_b_in = ''
        self._machine_b_out = '' #?

        if kwargs.has_key('retries'): #lol undocumented kwargs
            self._retries = kwargs['retries']
        else:
            self._retries = 0

        #ports and stuff yay
        self.machine_a_socket = incoming_socket
        self._machine_b_addr = outgoing_addr
        self._machine_b_port = outgoing_port

    def connect_in():
        raise NotImplementedError

    def connect_out(address, port):
        outgoing = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        outgoing.connect((address, port))
        return outgoing

    def udp_in(self):
        raise NotImplementedError

    def udp_out(self):
        raise NotImplementedError

    def main(self):
        try:
            retry_count = 0
            while retry_count <= self._retries:
                try:
                    outgoing_socket = connect_out(self._machine_b_addr,
                                                  self._machine_b_port)
                except socket.timeout:
                    retry += 1
            if retry_count > self._retries: #if we maxed out retries
                raise socket.error

        except socket.error:
            # TODO: actually handle this?
            # debug stuff yay :v
            pass

        #connection loop


# interpret args passed to program
# localaddr, localport, remoteaddr, remoteport

arg_parser = argparse.ArgumentParser(
    description = "Simple 1:1 proxy - Example usage: proxy.py -p 8080 \
                   -r 192.168.0.1 -d 80")
arg_parser.add_argument(
    '-l', '--local-addr', default = '0.0.0.0', dest = 'local_address',
    help = 'The local address to bind to (default: 0.0.0.0)')
arg_parser.add_argument(
    '-p', '--local-port', required = True, dest = 'local_port',
    help = 'The local TCP port to bind to')
arg_parser.add_argument(
    '-r', '--remote-addr', required = True, dest = 'remote_address',
    help = 'The remote address to connect to')
arg_parser.add_argument(
    '-d', '--remote-port', required = True, dest = 'remote_port',
    help = 'The remote port to connect to')

args = arg_parser.parse_args()
#apparently parse_args() will just close the program here if the user asks for
#help (-h)

#game/connection loop

threads = []
while True:
    try:
        #listen for stuff
        #when something connects, spawn a thread and try to establish the
        #outgoing connection 
        #profit
        parent_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #ipv4, tcp
        parent_socket.bind((args['local_address'], args['local_port']))
        parent_socket.listen() #might need to tweak backlog options later

        child_socket, child_addr_info = parent_socket.accept()

        child_thread = threading.Thread(
            target = Connection(child_socket,
                                args['remote_address'],
                                args['remote_port']).main()
            )

        child_thread.start()

        threads.append(child_thread)

    except KeyboardInterrupt:
        #clean up please
        break # <- this is not clean >:V