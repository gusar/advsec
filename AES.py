from Crypto.Cipher import AES


def aes_ecb_encrypt(plaintext, key):
    des_ecb = AES.new(key, AES.MODE_ECB)
    encrypted_result = des_ecb.encrypt(plaintext)
    return encrypted_result.encode('hex')


def aes_ecb_decrypt(ciphertext, key):
    des_ecb = AES.new(key, AES.MODE_ECB)
    ciphertext_hex = ciphertext.decode('hex')
    return des_ecb.decrypt(ciphertext_hex)


def aes_ecb_pad_encrypt(plaintext, key):
    padding_number = (len(key) - (len(plaintext) % len(key)))
    if padding_number < 10:
        padding = (padding_number - 2) * '\x00' + "%02d" % (padding_number,)
    else:
        padding = (padding_number - 2) * '\x00' + str(padding_number)
    padded_plaintext = plaintext + padding
    return aes_ecb_encrypt(padded_plaintext, key)


def aes_ecb_pad_decrypt(ciphertext, key):
    padded_plaintext = aes_ecb_decrypt(ciphertext, key)
    padding_number = int(padded_plaintext[-2:]) if '\x00' in padded_plaintext and int(padded_plaintext[-1:]) > 0 else 0
    return padded_plaintext[:-padding_number]

KEY = '1234567812345678'
PLAINTEXT = 'AAAABBBBCCCCDDDDAA\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0014'
CIPHERTEXT_base_16 = '43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD'
print('Encrypt ECB with padding:  ' + aes_ecb_pad_encrypt(PLAINTEXT, KEY))
print('Decrypt ECB with padding:  ' + aes_ecb_pad_decrypt(CIPHERTEXT_base_16, KEY))

# Q2
myFile = open('dictionary.txt', 'rw')
ciphertext = "43d3215c92a75a1478fcf9cb950d20dba628062fe8b278c4c21d0ea8f7179f16"
lines = myFile.readlines()
for line in lines:
    key = line.strip()
    print("Key: " + key)
    print("Encrypted text: " + ciphertext)
    print("Decrypted text: " + aes_ecb_pad_decrypt(ciphertext, key))