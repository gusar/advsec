def caesar(s, k, decrypt_flag=False):
    if decrypt_flag:
        k = 26 - k
    r = ""
    for i in s:
        if 65 <= ord(i) <= 90:
            r += chr((ord(i) - 65 + k) % 26 + 65)
        elif 97 <= ord(i) <= 122:
            r += chr((ord(i) - 97 + k) % 26 + 97)
        else:
            r += i
    return r


def encrypt(p, k):
    return caesar(p, k)


def decrypt(c, k):
    return caesar(c, k, True)

KEY = 2
TEST_STRING = 'Hello World'

caesar_encrypt_result_str = encrypt(TEST_STRING, KEY)
print('Encrypting "Hello World" with caesar no_decrypt=false:  {}'
      .format(caesar_encrypt_result_str))
decrypt_result_str = decrypt(caesar_encrypt_result_str, KEY)
print('Decrypting "{}":  {}\n'.format(caesar_encrypt_result_str, decrypt_result_str))
