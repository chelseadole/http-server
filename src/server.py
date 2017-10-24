"""."""

import socket


def server():
    """Creating server socket."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5001))
    server.listen(1)
    conn, addr = server.accept()

    conn.recv(10)

    msg = ''
    message_complete = False
    while not message_complete:
        part = conn.recv(10)
        print(part.decode('utf8'))
        msg += part
        if len(part) < 10:
            break

    conn.sendall('a reply from the server'.encode('utf8'))

    conn.close()
    server.close()
