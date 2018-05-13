from Crypto.PublicKey import RSA
from Crypto import Random
from File_operations import write_key

def newkeys(keysize):
    random_generator = Random.new().read
    key = RSA.generate(keysize, random_generator)
    private, public = key, key.publickey()
    return public, private

if __name__ =="__main__":
    key_size=1024*2
    (public, private)=newkeys(key_size)
    write_key("public.pem",public)
    write_key("private.pem",private)


