#!/usr/bin/env python3
from pra import pradec


def test_1():
    val = b'hello world'
    target = pradec.Hashes().Base64()
    target.decoded = val
    target.encoded = target.encode()
    assert target.encoded == b'aGVsbG8gd29ybGQ='


def test_2():
    val = b'aGVsbG8gd29ybGQ='
    target = pradec.Hashes().Base64()
    target.encoded = val
    target.decoded = target.decode()
    assert target.decoded == b'hello world'
