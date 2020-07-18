import hashlib

def enc_md5(plain):
    result = hashlib.md5(plain.encode())
    return result.hexdigest()

