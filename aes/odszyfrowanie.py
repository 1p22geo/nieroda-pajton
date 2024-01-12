from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os


key  = bytes()
with open('klucz', 'rb') as f:
    key = f.read()
    
cipher = AES.new(key, AES.MODE_EAX)

nonce  = bytes()
with open('plik.nonce', 'rb') as f:
    nonce = f.read()

ciphertext = bytes()

with open('plik', 'rb') as f:
    ciphertext = f.read()
    
tag = bytes()

with open('plik.tag', 'rb') as f:
    tag = f.read()



cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

with open('plik', 'wb') as f:
    f.write(data)

os.remove('plik.tag')
os.remove('plik.nonce')