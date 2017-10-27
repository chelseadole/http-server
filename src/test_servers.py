"""Tests for server and client sockets."""

import pytest


def test_server_response_ok():
    """Testing response ok 200 msg to client."""
    from server import server
    from server import response_ok
    assert server() == ok_200_msg


def test_msg_received_str():
    """Testing string received at server from client."""
    from server import server
    from client import client
    server()
    client()
    assert len(msg_received) > 2


def test_buffer_len():
    """."""
    from server import server


def test_response_ok():
    """Test response ok."""
    from server import response_ok
    assert response_ok() == b'HTTP/1.1 200 OK \n Content-Type: text/plain \n <CRLF> \n Message Received.'


def test_response_error():
    """Test response error."""
    from server import response_error
    assert response_error() == b'HTTP/1.1 500 Internal Server Error \n Content-Type: text/plain \n <CRLF> \n Server Error.'
