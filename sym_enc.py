#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import ARC4
import base64


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


def encode_mes(message):
    encoded_mes = base64.b64encode(message)
    return encoded_mes


def decode_mes(message):
    decoded_mes = base64.b64decode(message)
    return decoded_mes
