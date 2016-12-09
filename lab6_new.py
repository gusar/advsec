from Crypto.Cipher import ARC4


class StreamRC4:
    def __init__(self, key):
        self.key = key

    @property
    def arc4(self):
        return ARC4.new(self.key)

    def encrypt_rc4(self, text):
        return self.arc4.encrypt(text)

    def decrypt_rc4(self, text):
        return self.arc4.decrypt(text)


def main():
    key = 'mykey'
    plaintext = 'Programming is breaking of one big impossible task into several very small possible tasks'

    stream_rc4 = StreamRC4(key)
    result_ciphertext = stream_rc4.encrypt_rc4(plaintext)
    print('Plaintext:  ')
    print(result_ciphertext)

    ciphertext = result_ciphertext
    result_plaintext = stream_rc4.decrypt_rc4(ciphertext)
    print('\nCiphertext: ')
    print(result_plaintext)


if __name__ == '__main__':
    main()

