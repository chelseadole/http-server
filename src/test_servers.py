"""Tests for server and client sockets."""

from client import client


def test_msg_received_str():
    """Testing string received at server from client."""
    x = client('Hello world!')
    assert x == 'HTTP/1.1 200 OK\n\r\n\rContent-Type: text/plain\n\r\n\rMessage Received.'


def test_msg_received_two():
    """Test for buffer info."""
    x = client('This is a message with some info.')
    assert x == 'HTTP/1.1 200 OK\n\r\n\rContent-Type: text/plain\n\r\n\rMessage Received.'


def test_msg_with_ascii():
    """Test msg with ascii chars."""
    x = client('!@#$%^&*()')
    assert x == 'HTTP/1.1 200 OK\n\r\n\rContent-Type: text/plain\n\r\n\rMessage Received.'


def test_response_ok():
    """Test response ok."""
    from server import response_ok
    assert response_ok() == b'HTTP/1.1 200 OK\n\r\n\rContent-Type: text/plain\n\r\n\rMessage Received.'


def test_response_error():
    """Test response error."""
    from server import response_error
    assert response_error() == b'HTTP/1.1 500 Internal Server Error\n\r\n\rContent-Type: text/plain\n\r\n\rServer Error.'
