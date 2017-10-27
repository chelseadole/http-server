"""Test client and server module."""


import pytest


def test_message_sent_echo_back_the_same():
    """Test that message sent from client to server comes back."""
    from server import server
    from client import client
    server()
    x = client('hello')
    assert x == 'hello'
