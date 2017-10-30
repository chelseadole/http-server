"""Tests for server and client sockets."""

import pytest
import client


def test_that_request_for_text_file_returns_file_content():
    """Test that request for directory will return the content of the dirrectory in a list."""
    x = client('GET src HTTP/1.1\n\r\n\rContent-type: text/html\n\r\n\rHost: 127.0.0.1:5005')
    assert x = b"HTTP/1.1 200 OK\n\r\n\rContent-Type: text/html\n\r\n\r['__pycache__', 'client.py', 'client.pyc', 'server.py', 'test_servers.py']."