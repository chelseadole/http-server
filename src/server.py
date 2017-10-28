# -*- coding: utf-8 -*-
"""Server socket."""

from __future__ import unicode_literals
import socket


def server():
    """Server side socket."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5000))
    server.listen(1)

    try:
        while True:
            conn, addr = server.accept()
            buffer_stop = '§'.encode('utf8')
            msg_received = b''
            message_complete = False
            while not message_complete:
                part = conn.recv(10)
                msg_received += part
                if buffer_stop in part:
                    break

            print(msg_received.replace(buffer_stop, b''))
            msg = msg_received.replace(buffer_stop, b'')
            response = parse_request(msg)
            conn.sendall((response.encode('utf8')) + buffer_stop)

            conn.close()

    except KeyboardInterrupt:
        conn.close()
        server.close()


def response_ok():
    """200 Response."""
    return 'HTTP/1.1 200 OK\n\r\n\rContent-Type: text/plain\n\r\n\rMessage Received.'


def response_error(request_info):
    """Server Error or Client Error response for client."""
    if request_info == 'Method':
        return '501 Not Implemented Error\r\n\r\nServer Error'
    elif request_info == 'Protocol':
        return '505 HTTP Version Not Supported\r\n\r\nServer Error'
    elif request_info == 'Host':
        return '400 Bad Request\r\n\r\nClient Error'


def parse_request(request):
    """Parse request, validate or invalidate request."""
    request = request.decode('utf8')
    request_method, request_prot, host_tag, request_host = request.split()[0], request.split()[1], request.split()[2], request.split()[3]
    host, port = request_host.split(':')[0], request_host.split(':')[1]

    if request_method != 'GET':
        return response_error('Method')
    elif request_prot != 'HTTP/1.1':
        return response_error('Protocol')
    elif len(host.split('.')) != 4 or host.replace('.', '').isdigit() == False:
        return response_error('Host')
    elif host_tag != 'Host:':
        return response_error('Host')
    elif not port.isdigit():
        return response_error('Host')
    else:
        return response_ok()


if __name__ == '__main__':
    server()
