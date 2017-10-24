"""Client socket."""

import socket


def client(message):
    """Client side socket."""
    socket_info = socket.getaddrinfo('127.0.0.1', 5015)
    stream_info = [i for i in socket_info if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])

    client.sendall((message + '§').encode('utf8'))

    reply_from_server = ''
    buffer_stop = '§'
    message_incomplete = True
    while message_incomplete:
        part = client.recv(10)
        reply_from_server += part.decode('utf8')
        if buffer_stop in part.decode('utf8'):
            message_incomplete = False
    print(reply_from_server.replace(buffer_stop, ''))

    client.close()

if __name__ == '__main__':
    client(u'Un mensaje über importante con accentos éóí.')
