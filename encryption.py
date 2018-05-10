#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import ARC4

def rc4(msg):

    key = 'MyNameIsMammad'
    enc = ARC4.new(key)
    #msg = msg.encode('utf8')
    cipher = enc.encrypt(msg)
    return cipher
