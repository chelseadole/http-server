"""Tests for server and client sockets."""

import pytest
from client import client


def test_server_response_ok_if_get_request():
    """Testing response ok 200 msg to client."""
    x = client('GET /URI HTTP/1.1\r\n\r\nHost: 127.0.0.1:5000')
    assert x == 'HTTP/1.1 200 OK \n Content-Type: text/plain \n <CRLF> \n Message Received.'


# def test_msg_received_str():
#     """Testing string received at server from client."""
#     from server import server
#     from client import client
#     server()
#     client()
#     assert len(msg_received) > 2

# def test_buffer_len():
#     from server import server
    
