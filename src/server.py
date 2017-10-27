"""Server socket."""

import socket


def server():
    """Creating server socket."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5002))
    server.listen(1)
    try:
        conn, addr = server.accept()
        msg_recieved = ''
        buffer_length = 10
        message_complete = False
        while not message_complete:
            part = conn.recv(buffer_length)
            msg_recieved += part.decode('utf8')
            if len(part) < buffer_length:
                break

        print(msg_recieved)
        conn.sendall(msg_recieved.encode('utf8'))

        conn.close()

    except KeyboardInterrupt:
        conn.close()
        server.close()


if __name__ == '__main__':
    server()
