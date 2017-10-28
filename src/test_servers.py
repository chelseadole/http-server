"""Tests for server and client sockets."""

import pytest

# @pytest.fixture
#     def

# def test_server_response_ok():
#     """Testing response ok 200 msg to client."""
#     from server import server
#     from server import response_ok
#     assert server() == ok_200_msg


# def test_msg_received_str():
#     """Testing string received at server from client."""
#     from server import server
#     from client import client
#     server()
#     client()
#     assert len(msg_received) > 2


# def test_buffer_len():
#     from server import server
#     from client import client
#     assert client('')

def test_good_request():
    from server import server
    from client import client
    assert client(u'POST /URI HTTP/1.1\r\n\r\nHost: 127.0.0.1:5003') == b'HTTP/1.1 200 OK \n Content-Type: text/plain \n <CRLF> \n Message Received.'
