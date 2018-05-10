import encoding
import decoding
import encryption
import decription

a = "salam"
b = encryption.rc4(a)
b = encoding.encode_mes(b)
print(b)
c = decoding.decode_mes(b)
c = decription.decrption(c)
print(type(c))
