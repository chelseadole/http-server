"""Client socket."""

import socket


def client(message):
    """Client side socket."""
    socket_info = socket.getaddrinfo('127.0.0.1', 5010)
    stream_info = [i for i in socket_info if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])

    client.sendall((message + 'ai_coñ*').encode('utf8'))

    reply_from_server = ''
    message_incomplete = True
    while message_incomplete:
        part = client.recv(10)
        part.decode('utf8')
        if u'ai_coñ*'.decode('utf8') in part:
            message_incomplete = False
    print(reply_from_server)

    client.close()

if __name__ == '__main__':
    client(u'Un mensaje über importante con accentos éóí.')
