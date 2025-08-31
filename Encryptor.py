
def xor_encrypt(text, key):
    """הצפנה עם XOR להקסדצימל"""
    return ''.join(f"{ord(c) ^ ord(key[i % len(key)]):02x}"
                   for i, c in enumerate(text))




message = ("123456 jrciu bri$%% ^&*& jcnijcr46       \\\\\\\\\\")

key = "0123456789"

encrypted = xor_encrypt(message, key)
print(encrypted)




# def xor_decrypt(enc_hex, key):
#     """פענוח מטקסט מוצפן בהקס חזרה למחרוזת"""
#     return ''.join(chr(int(enc_hex[i:i+2], 16) ^ ord(key[(i//2) % len(key)]))
#                    for i in range(0, len(enc_hex), 2))

# decrypted = xor_decrypt(encrypted, key)
# print(decrypted)
