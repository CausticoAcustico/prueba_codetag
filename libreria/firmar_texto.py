from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 
from base64 import b64encode
import sys
import urllib2

def sign_data(private_key_loc, data):
    key = open(private_key_loc, "r").read() 
    rsakey = RSA.importKey(key) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new() 
    digest.update(data) 
    sign = signer.sign(digest) 
    return b64encode(sign)

texto = sys.argv[1]
llave_privada = sys.argv[2]

print urllib2.quote(sign_data(llave_privada,texto))