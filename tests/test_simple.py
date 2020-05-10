#!/usr/bin/env python3
from pradec import pradec
from pramon import pramon


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


def test_3():
    val = b'hello world'
    target = pradec.Hashes().Base64()
    target.decoded = val
    target.computeHash = pramon.createHash.__get__(target)
    assert target.computeHash() == '5eb63bbbe01eeed093cb22bb8f5acdc3'
