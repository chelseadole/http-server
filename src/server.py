# -*- coding: utf-8 -*-
"""Server socket."""

import socket


def server():
    """Server side socket."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(('127.0.0.1', 5002))
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
                if buffer_stop in part:
                    break

            print(msg_received.replace(buffer_stop, b''))
            conn.sendall(parse_request(msg_received) + buffer_stop)

            conn.close()

    except KeyboardInterrupt:
        conn.close()
        server.close()


def response_ok():
    """200 Response."""
    return b'HTTP/1.1 200 OK \n Content-Type: text/plain \n <CRLF> \n Message Received.'


def response_error(request_info):
    """Server Error or Client Error response for client."""
    print(request_info.split())
    if request_info == 'Method':
        return b'501 Not Implemented Error\r\n\r\nServer Error'
    elif request_info == 'Protocol':
        return b'505 HTTP Version Not Supported\r\n\r\nServer Error'
    elif request_info == 'Host':
        return b'400 Bad Request\r\n\r\nClient Error'
    else:
        response_ok()


def parse_request(request):
    """Parse request, validate or invalidate request."""
    request = request.decode('utf8')
    print(request.split())
    request_method, request_prot, host_tag, request_host = request.split()[0], request.split()[2], request.split()[3], request.split()[4]
    host, port = request_host.split(':')[0], request_host.split(':')[1]

    if request_method != 'GET':
        return response_error('Method')
    elif request_prot != 'HTTP/1.1':
        return response_error('Protocol')
    elif len(host.split('.')) != 4 or not [i.isdigit() for i in host.split('.')]:
        return response_error('Host')
    elif host_tag != 'Host:':
        return response_error('Host')
    elif not port.isdigit():
        return response_error('Host')
    else:
        return request.split()[1]


if __name__ == '__main__':
    server()
