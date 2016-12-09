from Crypto.Util import number

p = number.getPrime(8)

prime = p
num_to_check = 0
primitive_roots = []
for each in range(1, prime):
    num_to_check += 1
    candidate_prim_roots = []
    for i in range(1, prime):
        modulus = (num_to_check ** i) % prime
        candidate_prim_roots.append(modulus)
        cleaned_up_candidate_prim_roots = set(candidate_prim_roots)
        if len(cleaned_up_candidate_prim_roots) == len(range(1, prime)):
            primitive_roots.append(num_to_check)

g = int(primitive_roots[-1])
a = number.getRandomInteger(8)
b = number.getRandomInteger(8)
A = (g ^ a) % p
B = (g ^ b) % p
aliceSS = (B ^ a) % p
bobSS = (A ^ b) % p

print('g: ' + str(g))
print('a: ' + str(a))
print('b: ' + str(b))
print('A: ' + str(A))
print('B: ' + str(g))
print('Alice: ' + str(aliceSS))
print('Bob: ' + str(bobSS))
