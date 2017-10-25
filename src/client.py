# -*- coding: utf-8 -*-
"""Client socket."""

import socket


def client(message):
    """Client side socket."""
    socket_info = socket.getaddrinfo('127.0.0.1', 5003)
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

if __name__ == '__main__':
    client(u'POST /URI HTTP/1.1\r\n\r\nHost: 127.0.0.1:5000')


# sys.version_info.major == 3
# from __future__ import unicode-literals
