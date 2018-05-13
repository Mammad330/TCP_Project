from Crypto.PublicKey import RSA

def write_key(path, key):
    with open(path, "wb") as file:
        file.write(key.exportKey(format="PEM"))


def read_key(path):
    with open(path, "rb") as file:
        key = file.read()
        key_st=RSA.importKey(key)
    return key_st

