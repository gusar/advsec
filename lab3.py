from Crypto.Cipher import DES
key = '12345678'

def encrypt(key, plainText, mode, iv, padding):
    if (mode == DES.MODE_ECB):
        des = DES.new(key, mode)
        #add padding if text length not divisible by 8
        if (padding == True and len(plainText) % 8 != 0):
            paddingLength = len(plainText) % 8
            plainText += ' '  * paddingLength
    elif (mode == DES.MODE_CBC):
        des = DES.new(key, mode, iv)

    return des.encrypt(plainText).encode('hex')

def decrypt(key, cipherText, mode, iv, padding):
    if (mode == DES.MODE_ECB):
        des = DES.new(key, mode)
    elif (mode == DES.MODE_CBC):
        des = DES.new(key, mode, iv)

    return des.decrypt(cipherText.decode('hex'))

print "--------------------------Q1----------------------------------" 
text = 'AAAABBBBAAAABBBB'
cipherText = encrypt(key, text, DES.MODE_ECB, '', False)
print "Encrypted text: " + cipherText
print "Decrypted text: " + decrypt(key, cipherText, DES.MODE_ECB, '', False)

print "--------------------------Q2----------------------------------" 
text = 'AAAABBBBAAAABBBB'
iv = '00000000'
cipherText = encrypt(key, text, DES.MODE_CBC, iv, False)
print "Encrypted text: " + cipherText
print "Decrypted text: " + decrypt(key, cipherText, DES.MODE_CBC, iv, False)

print "--------------------------Q3----------------------------------"
text = 'AAAABBBBCCCC' 
cipherText = encrypt(key, text, DES.MODE_ECB, '', True)
print cipherText
decryptedText = decrypt(key, cipherText, DES.MODE_ECB, '', True)
print "Decrypted text: ", decryptedText, " length: ", len(decryptedText)