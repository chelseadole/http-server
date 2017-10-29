# -*- coding: utf-8 -*-
"""Server socket."""

from __future__ import unicode_literals
import socket
import os


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
            print(type(msg_received))
            print(type(buffer_stop))
            conn.sendall(parse_request(msg_received.replace(buffer_stop, b'')) + buffer_stop)

            conn.close()

    except KeyboardInterrupt:
        conn.close()
        server.close()


def response_ok(final_uri):
    """200 Response."""
    return 'HTTP/1.1 200 OK \n Content-Type: {} \n <CRLF> \n {}.'.format(final_uri[0], final_uri[1]).encode('utf8')


def response_error(request_info):
    """Server Error or Client Error response for client."""
    if request_info == 'Method':
        return b'501 Not Implemented Error\r\n\r\nServer Error'
    elif request_info == 'Protocol':
        return b'505 HTTP Version Not Supported\r\n\r\nServer Error'
    elif request_info == 'Host':
        return b'400 Bad Request\r\n\r\nClient Error'


def resolve_uri(content_type, uri):
    """Parse and redirect URIs to display information on terminal."""
    if os.path.isdir(uri):
        return content_type, os.listdir(uri)

    elif os.path.isfile(uri):
        # file = os.open(uri, os.O_RDONLY)
        # read_file = os.read(file, 9000)
        with open(uri) as file:
            read_file = file.read()
        return content_type, read_file


def parse_request(request):
    """Parse request, validate or invalidate request."""
    request = request.decode('utf8').replace(buffer_stop, '').split()        #'GET LICENSE HTTP/1.1\r\n\r\nContent-Type: text/html;\r\n\r\nHost: 127.0.0.1:5000'
    request_method, uri, request_prot, content_tag, content_type, host_tag, request_host = request[0], request[1], request[2], request[3], request[4], request[5], request[6]
    host, port = request_host.split(':')[0], request_host.split(':')[1]
    print(request)
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
        final_uri = resolve_uri(content_type, uri)
        return response_ok(final_uri)

if __name__ == '__main__':
    server()
