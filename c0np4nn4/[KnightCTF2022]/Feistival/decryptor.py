m, n = 21, 22
def f(word, key):
    out = ""
    for i in range(len(word)):
        out += chr(ord(word[i]) ^ key)
    return out

'''
flag = open("flag.txt", "r").read()

L, R = flag[0:len(flag)//2], flag[len(flag)//2:]
x = "".join(chr(ord(f(R, m)[i]) ^ ord(L[i])) for i in range(len(L)))
y = f(R, 0)

L, R = y, x
x = "".join(chr(ord(f(R, n)[i]) ^ ord(L[i])) for i in range(len(L)))
y = f(R, 0)

ciphertext = x + y
ct = open("cipher.txt", "w")
ct.write(ciphertext)
ct.close()
'''


ct = open("cipher.txt", "r").read()

L, R = ct[0:len(ct)//2], ct[len(ct)//2:]
y = f(R, 0)
x = "".join(chr(ord(f(y, n)[i]) ^ ord(L[i])) for i in range(len(L)))

L, R = x, y
y = f(L, 0)
x = "".join(chr(ord(f(y, m)[i]) ^ ord(R[i])) for i in range(len(R)))

plaintext = x + y
pt = open("plaintext.txt", "w")
pt.write(plaintext)
pt.close()

print(plaintext)
