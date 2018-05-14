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
    except Exception as e:
        print("Read file error: " + str(e))


def write_file_append(path, message):
    try:
        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, path)
        fo = open(abs_file_path, "ab+")
        fo.write(message)
        fo.close()
    except Exception as e:
        print("Write file error: " + str(e))


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
    try:
        with open(path, "wb") as file:
            file.write(key.exportKey(format="PEM"))
    except Exception as e:
        print("Writing key error: " + str(e))


def read_key(path):
    try:
        with open(path, "rb") as file:
            key = file.read()
            key_st = RSA.importKey(key)
        return key_st
    except Exception as e:
        print("Reading key error:" + str(e))
