from Crypto.Cipher import AES


key  = bytes()
with open('klucz', 'rb') as f:
    key = f.read()


cipher = AES.new(key, AES.MODE_EAX)

data = bytes()
with open('plik', 'rb') as f:
    data = f.read()


nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)

with open('plik', 'wb') as f:
    f.write(ciphertext)
with open('plik.tag', 'wb') as f:
    f.write(tag)
with open('plik.nonce', 'wb') as f:
    f.write(nonce)