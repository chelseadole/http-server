"""Client socket."""

import socket


def client(message):
    """Creating client socket."""
    socket_info = socket.getaddrinfo('127.0,0.1', 5001)
    stream_info = [i for i in socket_info if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])

    message = u'Un mensaje über importante con accentos éóí.'
    client.sendall(message.encode('utf8'))

    reply_complete = False
    while not reply_complete:
        part = client.recv(10)
        part(part.decode('utf8'))
        if len(part) < 10:
            break

    # client.close()
