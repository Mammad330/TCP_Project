#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import ARC4


def encyrption(msg1):
    key = 'MyNameIsMammad'
    enc = ARC4.new(key)
    # msg = msg.encode('utf8')
    cipher = enc.encrypt(msg1)
    return cipher


def decrption(msg2):
    key = 'MyNameIsMammad'
    enc = ARC4.new(key)
    # msg = msg.encode('utf8')
    cipher = enc.decrypt(msg2)
    return cipher.decode("ascii")
