from Crypto.Cipher import DES

# Q1
print('Q1')


def des_ecb_encrypt(plaintext, key):
    des_ecb = DES.new(key, DES.MODE_ECB)
    encrypted_result = des_ecb.encrypt(plaintext)
    return encrypted_result.encode('hex')


def des_ecb_decrypt(ciphertext, key):
    des_ecb = DES.new(key, DES.MODE_ECB)
    ciphertext_hex = ciphertext.decode('hex')
    return des_ecb.decrypt(ciphertext_hex)


KEY = "12345678"
PLAINTEXT = "AAAABBBBAAAABBBB"
CIPHERTEXT = "19FF4637BB2FE77C19FF4637BB2FE77C"

print('Encrypt ECB:  ' + des_ecb_encrypt(PLAINTEXT, KEY))
print('Decrypt ECB:  ' + des_ecb_decrypt(CIPHERTEXT, KEY))


# Q2
print('Q2')


def des_cbc_encrypt(plaintext, key, iv):
    des_cbc = DES.new(key, DES.MODE_CBC, iv)
    encrypted_result = des_cbc.encrypt(plaintext)
    return encrypted_result.encode('hex')


def des_cbc_decrypt(ciphertext, key, iv):
    des_cbc = DES.new(key, DES.MODE_CBC, iv)
    ciphertext_hex = ciphertext.decode('hex')
    return des_cbc.decrypt(ciphertext_hex)


KEY = "12345678"
IV = "00000000"
PLAINTEXT = "AAAABBBBAAAABBBB"
CIPHERTEXT = "AAC823F6BBE58F9EAF1FE0EB9CA7EB08"

print('Encrypt CBC:  ' + des_cbc_encrypt(PLAINTEXT, KEY, IV))
print('Decrypt CBC:  ' + des_cbc_decrypt(CIPHERTEXT, KEY, IV))


# Q3
# print('Q3')


def des_ecb_pad_encrypt(plaintext, key):
    padding_number = (len(key) - (len(plaintext) % len(key)))
    if padding_number < 10:
        padding = (padding_number - 2) * '\x00' + "%02d" % (padding_number,)
    else:
        padding = (padding_number - 2) * '\x00' + str(padding_number)
    padded_plaintext = plaintext + padding
    return des_ecb_encrypt(padded_plaintext, key)


def des_ecb_pad_decrypt(ciphertext, key):
    padded_plaintext = des_ecb_decrypt(ciphertext, key)
    padding_number = int(padded_plaintext[-2:]) if '\x00' in padded_plaintext else 0
    return padded_plaintext[:-padding_number]


KEY = "12345678"
PLAINTEXT = "AAAABBBBCCCC"
PLAINTEXT_WITH_PADDING = "AAAABBBBCCCC\x00\x0004"
CIPHERTEXT_base_16 = "19FF4637BB2FE77C81987E5CB99B66E2"

print('Encrypt ECB with padding:  ' + des_ecb_pad_encrypt(PLAINTEXT, KEY))
print('Decrypt ECB with padding:  ' + des_ecb_pad_decrypt(CIPHERTEXT_base_16, KEY))
