import time

start = time.time()
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from base64 import b16encode


# Loading private key
with open("private.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

message = ""
with open("message.txt", "r") as f:
    message = f.read()

message = bytes(message, encoding='utf-8') #print(bytes('hello', encoding='utf-8'))

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA3_256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA3_256()
)

signature = b16encode(signature)
signature = str(signature, 'utf-8')

with open("signature.txt", "w+") as f:
    f.write(signature)
end = time.time()
print(end - start)

