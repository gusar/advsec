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

# Answer
"""Xka F pexii objxfk pxqfpcfba, xka molra ql exsb ybbk qeb cfopq tel exp bsbo bkglvba qeb corfq
lc efp tofqfkdp xp criiv xp eb zlria abpfob; clo jv abpfob exp ybbk kl lqebo qexk ql abifsbo
lsbo ql qeb abqbpqxqflk lc jxkhfka qeb cxipb xka cllifpe qxibp lc qeb yllhp lc zefsxiov, tefze,
qexkhp ql qexq lc jv qorb Alk Nrfulqb, xob bsbk klt qlqqbofkd, xka alryqibpp alljba ql cxii
clo bsbo. Cxobtbii."""


# Q2

CIPHERTEXT = """Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur
zrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or
uvqvat ure sebz gur jbeyq"""

for key in range(1, 27):
    decrypt_result_str = decrypt(CIPHERTEXT, key)
    print("\nDecrypting using key {}:\n{}".format(str(key), decrypt_result_str))

# Answer: key 13
"""It would seem that, as he examined the several possibilities, a suspicion crossed his mind: the
memory of how he himself had behaved in earlier days made him ask whether someone might be
hiding her from the world"""