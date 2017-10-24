"""Server socket."""

import socket


def server():
    """Server side socket."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5010))
    server.listen(1)
    conn, addr = server.accept()

    msg_received = ''
    buffer_length = 10
    message_complete = False
    while not message_complete:
        part = conn.recv(buffer_length)
        msg_received += part.decode('utf8')
        if len(part) < buffer_length:
            break

    print(msg_received)
    conn.sendall(response_ok())

    conn.close()
    server.close()

    if KeyboardInterrupt:
        conn.close()
        server.close()


def response_ok():
    """200 Response."""
    return u'HTTP/1.1 200 OK \n Content-Type: text/plain \n <CRLF> \n Message Received.'.encode('utf8')


def response_error():
    """500 Server Error response for client."""
    error_500_msg = u'HTTP/1.1 500 Internal Server Error \n Content-Type: text/plain \n <CRLF> \n Server Error.'
    conn.sendall(error_500_msg.encode('utf8'))
    return error_500_msg

if __name__ == '__main__':
    server()
