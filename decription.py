#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import ARC4


def encyrption(msg):
    key = 'MyNameIsMammad'
    enc = ARC4.new(key)
    # msg = msg.encode('utf8')
    cipher = enc.encrypt(msg)
    return cipher


def decrption(msg):
    key = 'MyNameIsMammad'
    enc = ARC4.new(key)
    # msg = msg.encode('utf8')
    cipher = enc.decrypt(msg)
    return cipher.decode()
