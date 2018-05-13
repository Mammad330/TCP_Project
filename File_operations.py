import os
from Crypto.PublicKey import RSA

def read_file(path):
    try:
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, path)
        fo = open(abs_file_path, "r")
        file_list = fo.read()
        fo.close()
        return file_list
    except FileNotFoundError:
        print("No such a file")


def write_file_append(path, message):
    try:
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, path)
        fo = open(abs_file_path, "ab+")
        fo.write(message)
        fo.close()
    except FileNotFoundError:
        print("No such a file")

def write_file(path, message):
    try:
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, path)
        fo = open(abs_file_path, "w")
        fo.write(message)
        fo.close()
    except FileNotFoundError:
        print("No such a file")

def write_key(path, key):
    with open(path, "wb") as file:
        file.write(key.exportKey(format="PEM"))


def read_key(path):
    with open(path, "rb") as file:
        key = file.read()
        key_st=RSA.importKey(key)
    return key_st
