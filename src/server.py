# -*- coding: utf-8 -*-
"""Server socket."""

import socket


def server():
    """Server side socket."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5000))
    server.listen(1)

    try:
        while True:
            conn, addr = server.accept()
            msg_received = b''
            buffer_stop = b'\xa7'
            message_complete = False
            while not message_complete:
                part = conn.recv(10)
                msg_received += part
                print (msg_received)
                if buffer_stop in part:
                    break

            print(msg_received.replace(buffer_stop, b''))
            conn.sendall(response_ok() + buffer_stop)

            conn.close()

    except KeyboardInterrupt:
        conn.close()
        server.close()


def response_ok():
    """200 Response."""
    return b'HTTP/1.1 200 OK \n Content-Type: text/plain \n <CRLF> \n Message Received.'


def response_error():
    """500 Server Error response for client."""
    return b'HTTP/1.1 500 Internal Server Error \n Content-Type: text/plain \n <CRLF> \n Server Error.'


if __name__ == '__main__':
    server()
