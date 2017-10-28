# -*- coding: utf-8 -*-
"""Server socket, concurrent version."""

import socket
import sys
import os
import select


def server(log_buffer=sys.stderr):
    """Concurrent server."""
    address = ('127.0.0.1', 5003)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(address)
    server.listen(5)

    buffer_stop = b'\xa7'
    buff_size = 10

    channels = [server, sys.stdin]
    server_running = True

    while server_running:

        read_ready, write_ready, except_ready = select.select(channels, [], [], 0)

        for msg in read_ready:

            if msg is server:
                handler_socket, address = msg.accept()
                channels.append(handler_socket)

            elif msg is sys.stdin:
                sys.stdin.readline()
                server_running = False

            else:
                msg_received = b''
                message_complete = False
                while message_complete:
                    part = msg.recv(buff_size)
                    msg_received += part
                    if buffer_stop in part:
                        message_complete = True
                print(msg_received.replace(buffer_stop, b''))
                msg.sendall(parse_request(msg_received) + buffer_stop)

    server.close()


def response_ok(final_uri):
    """200 Response."""
    return 'HTTP/1.1 200 OK\nContent-Type: {}\n\r\n\r{}.'.format(final_uri[0], final_uri[1]).encode('utf8')


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
    request = request.decode('utf8').replace('§', '').split()

    request_method, uri, request_prot, content_type, host_tag, request_host = request[0], request[1], request[2], request[4], request[5], request[6]
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
        final_uri = resolve_uri(content_type, uri)
        print (final_uri)
        return response_ok(final_uri)

if __name__ == '__main__':
    server()
