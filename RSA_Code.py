from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256  # from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5


def encrypt_asym(message, pub_key):
    try:
        # RSA encryption protocol according to PKCS#1 OAEP
        cipher = PKCS1_OAEP.new(pub_key)
        return cipher.encrypt(message)
    except Exception as e:
        print("Asymmetric encryption error: " + str(e))


def decrypt_asym(ciphertext, priv_key):
    try:
        # RSA encryption protocol according to PKCS#1 OAEP
        cipher = PKCS1_OAEP.new(priv_key)
        return cipher.decrypt(ciphertext).decode()
    except Exception as e:
        print("Asymmetric decryption error: " + str(e))


def sign(message, priv_key, ):
    try:
        signer = PKCS1_v1_5.new(priv_key)
        digest = SHA256.new()
        digest.update(message)
        return signer.sign(digest)
    except Exception as e:
        print("Sign message error: " + str(e))


def verify(message, signature, pub_key):
    try:
        signer = PKCS1_v1_5.new(pub_key)
        digest = SHA256.new()
        digest.update(message)
        return signer.verify(digest, signature)
    except Exception as e:
        print("Verification of sign error: " + str(e))
