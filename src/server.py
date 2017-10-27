# -*- coding: utf-8 -*-
"""Server socket."""

from __future__ import unicode_literals
import socket


def server():
    """Creating server socket."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5006))
    server.listen(1)
    try:
        while True:
            conn, addr = server.accept()
            msg_received = b''
            buffer_stop = '§'.encode('utf8')
            message_complete = False
            while not message_complete:
                part = conn.recv(10)
                msg_received += part
                if buffer_stop in part:
                    break

            print(msg_received.replace(buffer_stop, b''))
            conn.sendall(msg_received + buffer_stop)

            conn.close()

    except KeyboardInterrupt:
        conn.close()
        server.close()


if __name__ == '__main__':
    server()
