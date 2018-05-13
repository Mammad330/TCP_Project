from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
# from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode

from decription import encyrption, decrption
from decoding import decode_mes, encode_mes


def newkeys(keysize):
    random_generator = Random.new().read
    key = RSA.generate(keysize, random_generator)
    private, public = key, key.publickey()
    return public, private


def getpublickey(priv_key):
    return priv_key.publickey()


def encrypt(message, pub_key):
    # RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(message)


def decrypt(ciphertext, priv_key):
    # RSA encryption protocol according to PKCS#1 OAEP
    cipher = PKCS1_OAEP.new(priv_key)
    return cipher.decrypt(ciphertext)


def sign(message, priv_key, ):
    signer = PKCS1_v1_5.new(priv_key)
    digest = SHA256.new()
    digest.update(message)
    return signer.sign(digest)


def verify(message, signature, pub_key):
    signer = PKCS1_v1_5.new(pub_key)
    digest = SHA256.new()
    digest.update(message)
    return signer.verify(digest, signature)


def write_key(path, key):
    with open(path, "wb") as file:
        file.write(key.exportKey(format="PEM"))


def read_key(path):
    with open(path, "rb") as file:
        key = file.read()
        key_st = RSA.importKey(key)
    return key_st


msg1 = b"Hello Tony, I am Jarvis!"
keysize = 2048
(public, private) = newkeys(keysize)
write_key("private.pem", private)
private_read = read_key("private.pem")
write_key("public.pem", public)
public_read = read_key("public.pem")

encrypted = encyrption(msg1)
encoded_encrypted = encode_mes(encrypted)
decoded = decode_mes(encoded_encrypted)
decrypted = decrption(decoded)
# encrypted = b64encode(encrypt(msg1, public_read))

# decrypted = decrypt(b64decode(encrypted), private_read)

print(encoded_encrypted)
print(decrypted.encode())
# print(public_read.exportKey("PEM"))
# print(private_read.exportKey("PEM"))
signature = b64encode(sign(encoded_encrypted, private_read))
verify1 = verify(encoded_encrypted, b64decode(signature), public_read)

# print(private.exportKey('PEM'))
# print(public.exportKey('PEM'))
# print("Encrypted: " + str(encrypted))
# print("Decrypted: '%s'" % decrypted)
print("Signature: " + str(signature))
print("Verify: %s" % verify1)
# print(verify(msg2, b64decode(signature), public))
