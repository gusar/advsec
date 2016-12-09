import hmac
from hashlib import md5
from hashlib import sha256
from hashlib import sha512 

def compare(key, message, alg, mac):
    return str(hmac.compare_digest(hmac.new(key, message, alg).hexdigest(), mac))

message = 'AAAABBBBCCCC'
key = '123456789'
m = hmac.new(key, message, md5).hexdigest()
s256 = hmac.new(key, message, sha256).hexdigest()
s512 = hmac.new(key, message, sha512).hexdigest()

print 'Message: ' + message
print 'Key: ' + key
print 'MD5: ' + m
print 'SHA256: ' + s256
print 'SHA512: ' + s512

print '>>>Authenticate message<<<'
print 'MD5: ' + compare(key, message, md5, m)
print 'SHA256:' + compare(key, message, sha256, s256)
print 'SHA512: ' + compare(key, message, sha512, s512)