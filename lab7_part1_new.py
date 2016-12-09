import base64
from Crypto.Cipher import DES

BYTE = 8


class HashDES:
    def __init__(self, key):
        self.key = key

    @property
    def des(self):
        return DES.new(self.key, DES.MODE_ECB)

    @staticmethod
    def pad(plaintext):
        padding_len = BYTE - (len(plaintext) % BYTE)
        plaintext += "\x00" * padding_len
        return plaintext

    @staticmethod
    def byte_split(string, length):
        return [string[i:i + length] for i in range(0, len(string), length)]

    @staticmethod
    def encode_base16(hashed_text):
        return base64.b16encode(hashed_text)

    def hash(self, plaintext):
        padded_ptext = self.pad(plaintext)
        partitioned_plaintext = self.byte_split(padded_ptext, BYTE)
        # hash iteratively each time using previous hashing result and each consecutive plaitext block
        _hash = self.key
        for part in partitioned_plaintext:
            _hash = self._encrypt_part(_hash, part)
        return _hash

    def _encrypt_part(self, _hash, part):
        ciphertext = self.des.encrypt(part)
        # XOR each char of ciphertext with each respective char of key
        xored_char_list = [chr(ord(x) ^ ord(y)) for x, y in zip(_hash, ciphertext)]
        return ''.join(xored_char_list)


def main():
    key = "00000000"
    plaintext = "AAAABBBBCCCCD"
    hash_des = HashDES(key)
    hashed_text = hash_des.hash(plaintext)
    hashed_text_base16 = hash_des.encode_base16(hashed_text)

    print('Plaintext: ' + plaintext)
    print('Hash in base16: ' + hashed_text_base16)


if __name__ == '__main__':
    main()
