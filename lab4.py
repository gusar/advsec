from Crypto.Cipher import AES
key = '1234567812345678'

def encrypt(key, plainText, mode, iv):
    aes = AES.new(key, mode)
    #add padding if text length not divisible by 16
    if (len(plainText) % 16 != 0):
        paddingLength = 16 - (len(plainText) % 16)
        plainText += ' '  * paddingLength

    return aes.encrypt(plainText).encode('hex')

def decrypt(key, cipherText, mode, iv):
    aes = AES.new(key, mode)

    return aes.decrypt(cipherText.decode('hex'))

print "--------------------------Q1----------------------------------" 
text = 'AAAABBBBCCCCDDDDAA'
cipherText = encrypt(key, text, AES.MODE_ECB, '')
print "Encrypted text: " + cipherText
print "Decrypted text: " + decrypt(key, cipherText, AES.MODE_ECB, '')