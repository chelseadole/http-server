"""Client socket."""

import socket


def client(message):
    """Creating client socket."""
    socket_info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in socket_info if i[1] == socket.SOCK_STREAM][0]

    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall((message + '§').encode('utf8'))

    buffer_stop = '§'
    response_msg = ''
    reply_complete = False
    while not reply_complete:
        part = client.recv(10)
        response_msg += part.decode('utf8')
        if buffer_stop in response_msg:
            break

    print (response_msg.decode('utf8'))
    client.close()
    return(response_msg)


if __name__ == '__main__':
    import sys
    client(str(' '.join(sys.argv[1:len(sys.argv)])))
