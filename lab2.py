# -*- coding: utf-8 -*-


# CAESAR #
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

# Q1
KEY = -3
PLAINTEXT = """And I shall remain satisfied, and proud to have been the first who has ever enjoyed the fruit
of his writings as fully as he could desire; for my desire has been no other than to deliver
over to the detestation of mankind the false and foolish tales of the books of chivalry, which,
thanks to that of my true Don Quixote, are even now tottering, and doubtless doomed to fall
for ever. Farewell."""

caesar_encrypt_result_str = encrypt(PLAINTEXT, KEY)
print('Encrypting with key {}:  {}'.format(str(KEY), caesar_encrypt_result_str))


# Q2
CIPHERTEXT = """Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur
zrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or
uvqvat ure sebz gur jbeyq"""

for key in range(1, 27):
    decrypt_result_str = decrypt(CIPHERTEXT, key)
    print("\nDecrypting using key {}:\n{}".format(str(key), decrypt_result_str))


# VIGENERE #
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def translate(message, cipher_key, mode):
    result = []
    index = 0
    cipher_key = cipher_key.upper()

    for char in message:  # loop through chars in message
        position = LETTERS.find(char.upper())
        if position != -1:
            if mode == 'encrypt':
                position += LETTERS.find(cipher_key[index])
            elif mode == 'decrypt':
                position -= LETTERS.find(cipher_key[index])
            position %= len(LETTERS)

            # add symbol to the end of result.
            if char.isupper():
                result.append(LETTERS[position])
            elif char.islower():
                result.append(LETTERS[position].lower())

            index += 1
            if index == len(cipher_key):
                index = 0

        else:
            result.append(char)

    return ''.join(result)


def vigenere_encrypt(message, cipher_key):
    return translate(message, cipher_key, 'encrypt')


def vigenere_decrypt(message, cipher_key):
    return translate(message, cipher_key, 'decrypt')

# Q1
TEXT = "I shall (from now on) select and take the ingots individually in my own yard, " \
       "and I shall exercise against you my right of rejection because you have treated me with contempt."
KEY = "PASSWORD"
CIPHERTEXT = vigenere_encrypt(TEXT, KEY)
print("Encrypted text: {}".format(CIPHERTEXT))

# Q2
CIPHERTEXT = "Yhwvtroi, 28 Yudq 2016 - Pse bjatw pt foxgf zwjzql bgio qcwelwlar, blsg rmprochek ewrv nsoyr uvs ndcljebv rk pkium hy bef; sjr wutm vljg aybefl ds ydx mchf asx bojw lwfxx, aph fjsbntzaju kkwixit hvbduyzkik wme ylpzs gdrdv. wbu wme mmou olhtsajg wutm mmmzwxv lanebx ejipkt, obn dtzwn avq fnf xicgo lhg sns yxstuqfb oxs fakdsipjn qj uvs uxny zwjv gjskwusr pgoe zqbklsg, cre wt cdmw oafv lstgqqsfkie, lzam ydae eibgsn urge pvvlw ipxfadogafua oj zfs kr uvssg pgoaf; rqi odiewsxi tg ldszu kavlff oxs mgldsi dsd vs uvs oadwjo, we rupqwjhwyc tg lds gdxt cptc wx ihw xqhluj, ba wp oqdxny gj smhwy qgdogsdn, lzam nlql nmws poitwj wbu ptrg lbddsay"
KNOWN_PLAINTEXT = 'Thursday'
DICTIONARY = ['tiger', 'FACEBOOKPASSWORD', 'trustno1', 'alex', 'apple', 'avalon', 'brandy', 'chelsea', 'coffee', 'falcon', 'freedom',
              'gandalf', 'green', 'helpme', 'linda']


def dictionary_atack(dictionary, known_plaintext, ciphertext):
    for _key in dictionary:
        plaintext = vigenere_decrypt(ciphertext, _key)
        if known_plaintext in plaintext:
            print('\nPlaintext: ' + plaintext)
            return _key
    return None

KEY = dictionary_atack(DICTIONARY, KNOWN_PLAINTEXT, CIPHERTEXT)
if KEY:
    print('The key is: {}'.format(KEY))
else:
    print('No key found')
