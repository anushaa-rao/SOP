# importing the hashlib module
import hashlib

# the string will be hashed using the 'sha256'
name = 'to test code'
# convert the string to bytes using 'encode'

encoded_name = name.encode()

hashed_name = hashlib.sha256(encoded_name)

print("name", hashed_name)
print("Hexadecimal format:", hashed_name.hexdigest())
