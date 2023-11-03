from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils
import time

    
    
    

    

file = input("co odszyfrować: ")
kfile = input("podaj klucz prywatny: ")
pw = input("jakie hasło wariacie: ")

with open(kfile, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=pw.encode('utf-8'),
    )

text = b""
with open(file, 'rb') as f:
    text = f.read()
    
    
text = private_key.decrypt(
    text,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open(file, 'wb') as f:
    f.write(text)