from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import utils
import time
    
    

    
print("kogo zabić: ")
time.sleep(0.5)
file = input("to znaczy zaszyfrować: ")
kfile = input("podaj klucz publiczny: ")

with open(kfile, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

text = b""
with open(file, 'rb') as f:
    text = f.read()
    
    
text = public_key.encrypt(text, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))

with open(file, 'wb') as f:
    f.write(text)