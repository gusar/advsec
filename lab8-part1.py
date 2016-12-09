prime = 23
base = 5
aliceSecret = 6
bobSecret = 15

def encrypt(privateKey):
    return (base ** privateKey) % prime

def decrypt(message, secretKey):
    return (message ** secretKey) % prime

print 'Prime:' + str(prime), 'Base:'+ str(base)
# Alice chooses a secret
alicePublic = encrypt(aliceSecret)
print('\nAlice Sends Over Public Channel: '+ str(alicePublic))
# Bob chooses a secret
bobPublic = encrypt(bobSecret)
print('Bob Sends Over Public Channel: '+ str(bobPublic))
# Alice Computes
aliceSharedSecret = decrypt(bobPublic, aliceSecret)
print('\nAlice Shared Secret: ' + str(aliceSharedSecret))
# Bob Computes
bobSharedSecret = decrypt(alicePublic, bobSecret)
print('Bob Shared Secret: '+ str(bobSharedSecret))

