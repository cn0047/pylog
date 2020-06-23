""" This module contains integrational tests for REAL-TIME log  client. """

import pytest

from realtimelog import Client


def test_client_with_id():
    id = 'this_is_test_id'
    c = Client(id)
    actual = c.get_url()
    assert id in actual


def test_client_without_id():
    c = Client()
    actual = c.get_url()
    assert 'https://realtimelog.herokuapp.com' in actual


def test_client_get_url():
    id = 'this_is_expected_id'
    c = Client(id)
    actual = c.get_url()
    assert id in actual


def test_client_msg():
    m = 'This is unit test from pylog package. If you see it - it means: it works!'
    id = 'publiclog'
    print(id)
    c = Client(id)
    c.msg({'id': id, 'message': m})
