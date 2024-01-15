import hmac
import hashlib

def calculate_hash(k, plaintext):
    k = bytes(k, "utf-8")
    plaintext = bytes(plaintext, "utf-8")
    calc = hmac.new(k, plaintext, hashlib.sha256)
    return calc.hexdigest()
    
comp_mac = calculate_hash("AdoptedBrotherOfThor", "Loki is a real hero!")
print(comp_mac)