"""Client socket."""

import socket
import sys


def client(message):
    """Creating client socket."""
    socket_info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in socket_info if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))

    response_msg = ''
    reply_complete = False
    while not reply_complete:
        part = client.recv(10)
        response_msg += part.decode('utf8')
        if len(part) < 10:
            break

    print (response_msg)
    client.close()


if __name__ == '__main__':
    client(str(' '.join(sys.argv[1:len(sys.argv)])))
