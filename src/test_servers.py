"""Tests for server and client sockets."""

import pytest
from client import client


def test_server_response_ok_if_get_request():
    """Test that a get request returns response ok 200 msg to client."""
    x = client('GET HTTP/1.1\r\n\r\nHost: 127.0.0.1:5000')
    assert x == 'HTTP/1.1 200 OK \n Content-Type: text/plain \n <CRLF> \n Message Received.'


def test_server_response_error_if_not_get_request():
    """Test that a post request returns a 501 error message."""
    x = client('POST HTTP/1.1\r\n\r\nHost: 127.0.0.1:5000')
    assert x == '501 Not Implemented Error\r\n\r\nServer Error'


def test_server_response_error_if_not_correct_http_request():
    """Test that a non http 1.1 request returns a 505 error message."""
    x = client('GET HTTP/2.1\r\n\r\nHost: 127.0.0.1:5000')
    assert x == '505 HTTP Version Not Supported\r\n\r\nServer Error'


def test_server_response_error_if_not_correct_host_request():
    """Test that if host is not valid ip address format a 400 bad request returns."""
    x = client('GET HTTP/1.1\r\n\r\nHost: 127.a.b.1:5000')
    assert x == '400 Bad Request\r\n\r\nClient Error'

# PARAMS = [('HTTP/1.1 GET\r\n\r\nHost: 127.0.0.1:5000', '501 Not Implemented Error\r\n\r\nServer Error'),
#           ('GET HTTP/1.1\r\n\r\nHost: 5000:127.0.0.1', '501 Not Implemented Error\r\n\r\nServer Error'),
#           ('GET Host:\r\n\r\nHTTP/1.1: 127.0.0.1:5000', '501 Not Implemented Error\r\n\r\nServer Error')]


# @pytest.mark.parametrize('request, response', PARAMS)
# def test_if_request_not_in_proper_order_error_message_recieved(request, response):
#     """Test if request is not properly formed 501 error message recieved."""
#     assert client(request) == response
