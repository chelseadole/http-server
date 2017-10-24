"""."""

import socket


def server():
    """Creating server socket."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5000))
    server.listen(1)
    conn, addr = server.accept()

    # conn.recv(10)

    msg_recieved = ''
    msg_sent = 'Roger, this is the server, I hear you loud and clear!'
    buffer_length = 10
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        msg_recieved += part.decode('utf8')
        if len(part) < buffer_length:
            break

    conn.sendall(msg_sent.encode('utf8'))

    conn.close()
    server.close()
