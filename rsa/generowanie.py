from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

with open("klucze/klucz", 'wb') as file:
    pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(b'pass')
    )
    print(pem.decode('ascii'))
    file.write(pem)
    
with open("klucze/klucz.pub", 'wb') as file:
    pem2 = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.PKCS1
    )
    print(pem2.decode('ascii'))
    file.write(pem2)