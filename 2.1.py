import numpy as np

def encrypt(plaintext,key):

    n2 = len(key)
    n1 = int(n2**0.5)
    keymatrix = np.array([[ord(key[i])-ord('A') for i in range(j*n1,(j+1)*n1)] for j in range(0,n1)])
    tokenArray = np.array([[ord(plaintext[i*n1 + j]) - ord('A') for i in range(int(len(plaintext)/n1))] for j in range(n1)])

    out = ''
    for i in range(int(len(plaintext)/n1)):
        t = keymatrix.dot(tokenArray[:,i])
        for j in range(len(t)):
            out += chr(ord('A')+t[j]%26)
    return out

key = input()
plaintext = input()
print(encrypt(plaintext,key))
