"""Client socket."""

import socket


def client(message):
    """Client side socket."""
    socket_info = socket.getaddrinfo('127.0.0.1', 5008)
    stream_info = [i for i in socket_info if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])

    client.sendall(message.encode('utf8'))

    reply_from_server = ''
    reply_complete = False
    while not reply_complete:
        part = client.recv(10)
        reply_from_server += part.decode('utf8')
        if len(part) < 10:
            break
    print(reply_from_server)

    client.close()

if __name__ == '__main__':
    client(u'Un mensaje über importante con accentos éóí.')
