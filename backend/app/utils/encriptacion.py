import hashlib
from hmac import compare_digest

def sign(entrada):
    encriptacion = hashlib.sha3_512(entrada.encode('utf-8'))
    return encriptacion.hexdigest()

def verify(entrada1,encrip2):
    encrip1 = sign(entrada1)
    return compare_digest(encrip1,encrip2)