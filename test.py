from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
# from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
import generate_keys


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


msg1 = b"Hello Tony, I am Jarvis!"
msg2 = b"Hello Toni, I am Jarvis!"
keysize = 2048
(public, private) = newkeys(keysize)
generate_keys.write_key("private.pem",private)
private_read=generate_keys.read_key("private.pem")
generate_keys.write_key("public.pem",public)
public_read=generate_keys.read_key("public.pem")
encrypted = b64encode(encrypt(msg1, public_read))

decrypted = decrypt(b64decode(encrypted), private_read)

print(encrypted)
print(decrypted)
print(public_read.exportKey("PEM"))
print(private_read.exportKey("PEM"))
signature = b64encode(sign(encrypted, private))
verify1 = verify(encrypted, b64decode(signature), public)

# print(private.exportKey('PEM'))
# print(public.exportKey('PEM'))
# print("Encrypted: " + str(encrypted))
# print("Decrypted: '%s'" % decrypted)
print("Signature: " + str(signature))
print("Verify: %s" % verify1)
# print(verify(msg2, b64decode(signature), public))
