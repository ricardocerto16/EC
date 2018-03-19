from cryptography.hazmat.backends   import default_backend
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

default_algorithm = hashes.SHA256
# seleciona-se um dos vários algorimos implementados na package

def hashs(s):
    digest = hashes.Hash(default_algorithm(),backend=default_backend())
    digest.update(s)
    return digest.finalize()

def mac(key,source, tag= None):
    h = hmac.HMAC(key,default_algorithm(),default_backend())
    h.update(source)
    if tag == None:
        return h.finalize() 
    h.verify(tag)

def kdf(salt):
    return PBKDF2HMAC(
        algorithm=default_algorithm(),   # SHA256
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()        # openssl
        )   