# vulnerable_code.py 
 
from cryptography.hazmat.primitives.asymmetric import rsa 
 
# This RSA key is vulnerable to Shor's algorithm 
key = rsa.generate_private_key(public_exponent=65537, key_size=2048) 
