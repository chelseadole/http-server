"""Test client and server module."""


import pytest
from client import client


def test_message_shorter_than_buffer_sent_echo_back_the_same():
    """Test that message sent from client to server comes back."""
    x = client('hello')
    assert x == 'hello'


def test_message_longer_than_buffer_sent_echo_back_the_same():
    """Test that message longer than buffer length echos back the same."""
    x = client('Hey what are you doing tonight?')
    assert x == 'Hey what are you doing tonight?'


def test_message_sent_exact_lenght_of_buffer_echo_back():
    """Test that message same length as buffer echos back the same."""
    x = client('want snow?')
    assert x == 'want snow?'
