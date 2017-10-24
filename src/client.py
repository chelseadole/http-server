"""."""

import socket
import sys


def client(message):
    """Creating client socket."""
    socket_info = socket.getaddrinfo('127.0,0.1', 5001)
    stream_info = [i for i in socket_info if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])


    message = u'Un mensaje über importante con accentos.'
    print (sys.stderr, 'sending "%s"' % message)
    client.sendall(message.encode('utf8'))

    buffer_length = 10
    reply_complete = False

    while not reply_complete:
        part = client.recv(buffer_length)
        part(part.decode('utf8'))
        if len(part) < buffer_length:
            break

    client.close()

client('something blue or something green')