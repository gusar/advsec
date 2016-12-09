import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

def encrypt(publicKey, message):
    cipherText = publicKey.encrypt(message, 32)

    # SEE: http://stackoverflow.com/questions/19338209/how-to-fix-a-typeerror-tuple-object-does-not-support-item-assignment
    cipherText = list(cipherText)
    cipherText[0] = cipherText[0].encode('hex')
    cipherText = tuple(cipherText)

    return cipherText

def decrypt(key, cipherText):
    # SEE: http://stackoverflow.com/questions/19338209/how-to-fix-a-typeerror-tuple-object-does-not-support-item-assignment
    cipherText = list(cipherText)
    cipherText[0] = cipherText[0].decode('hex')
    cipherText = tuple(cipherText)

    return key.decrypt(ast.literal_eval(str(cipherText)))

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key
publicKey = key.publickey() # pub key export for exchange

cipherText = encrypt(publicKey, 'Hello World!')
#message to encrypt is in the above line 'Hello world!'

print 'Ciphertext: ', cipherText[0] #Ciphertext

#decrypted text below
decryptedText = decrypt(key, cipherText)
print 'Decrypted text: ', decryptedText
