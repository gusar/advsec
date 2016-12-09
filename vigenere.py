import re
from itertools import cycle

ALPHA = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(key, plaintext):
    """Encrypt the string and return the ciphertext"""
    pairs = zip(plaintext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) + ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result.lower()


def decrypt(key, ciphertext):
    """Decrypt the string and return the plaintext"""
    pairs = zip(ciphertext, cycle(key))
    result = ''

    for pair in pairs:
        total = reduce(lambda x, y: ALPHA.index(x) - ALPHA.index(y), pair)
        result += ALPHA[total % 26]

    return result


def show_result(plaintext, key):
    """Generate a resulting cipher with elements shown"""
    encrypted = encrypt(key, plaintext)
    decrypted = decrypt(key, encrypted)

    print 'Key: %s' % key
    print 'Plaintext: %s' % plaintext
    print 'Encrytped: %s' % encrypted
    print 'Decrytped: %s' % decrypted


PLAINTEXT = """I shall (from now on) select and take the ingots individually in my own yard, and I shall
exercise against you my right of rejection because you have treated me with contempt."""
KEY = "PASSWORD"

# show_result(PLAINTEXT, KEY)


def encrypt_vigenere(plaintext, key):
    clean_plaintext = re.sub(r'\W+', '', plaintext)
    clean_plaintext_len = len(clean_plaintext)
    text_len = len(plaintext)

    matching_key_remainder = clean_plaintext_len % len(key)
    matching_key = (key * (clean_plaintext_len / len(key) + 1))[:-matching_key_remainder]

    key_text = ""
    count_len = 0
    while count_len < text_len:
        key_text += key
        count_len += len(key)
    key_text += key
    encrypt_text = ""
    final_text = ""

    for x in range(0, text_len):
        encrypt_text += key_text[x]

    for i in range(0, text_len):
        let_val = plaintext[i]

        text_no = ALPHA.index(let_val) + 1

        enc_val = encrypt_text[i]

        enc_no = ALPHA.index(enc_val)
        encrypt_no = (enc_no + text_no) % 26
        final_text += ALPHA[encrypt_no - 1]

    print(final_text)

encrypt_vigenere(PLAINTEXT, KEY)
