#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Crypto.Cipher import ARC4
import base64


def encyrption(msg):
    try:
        key = 'MyNameIsMammad'
        enc = ARC4.new(key)
        # msg = msg.encode('utf8')
        cipher = enc.encrypt(msg)
        return cipher
    except Exception as e:
        print("Symmetric encryption error:  " + str(e))


def decrption(msg):
    try:
        key = 'MyNameIsMammad'
        enc = ARC4.new(key)
        # msg = msg.encode('utf8')
        cipher = enc.decrypt(msg)
        return cipher.decode()
    except Exception as e:
        print("Symmetric decription error: " + str(e))


def encode_mes(message):
    try:
        encoded_mes = base64.b64encode(message)
        return encoded_mes
    except Exception as e:
        print("Encoding error:" + str(e))


def decode_mes(message):
    try:
        decoded_mes = base64.b64decode(message)
        return decoded_mes
    except Exception as e:
        print("Decoding error:" + str(e))
