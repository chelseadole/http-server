# -*- coding: utf-8 -*-
"""Module for client socket."""

import socket


def client(message):
    """Create a client side socket to send a request to server."""
    socket_info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in socket_info if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])

    client.sendall((message + '§').encode('utf8'))

    reply_from_server = b''
    buffer_stop = b'\xa7'
    message_incomplete = True
    while message_incomplete:
        part = client.recv(10)
        reply_from_server += part
        if buffer_stop in part:
            message_incomplete = False
    print(reply_from_server.replace(buffer_stop, b'').decode('utf8'))
    client.close()
    return(reply_from_server.replace(buffer_stop, b'').decode('utf8'))

if __name__ == '__main__':
    client('Un mensaje über importante con accentos éóí.')
