from cryptography.hazmat.primitives import serialization

with open("klucze/klucz", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=b'pass',
    )
    
with open("klucze/klucz.pub", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )
    
    
print(private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(b'pass')).decode("ascii")
      )

print(public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.PKCS1
    ).decode("ascii"))