#Cifra de César: substitui uma letra pela 3º casa à frente
#a - d
#b - e
#c - f
#x - a
#i - l

#abacaxi - defdfal

key = 3
message = 'Fala rapaziada, essa APS vai ficar pica kkk slc'
message = message.lower()
nA = ord('A')
nZ = ord('Z')
na = ord('a')
nz = ord('z')
n = 128
encryptor = ''
for i in message:
    ind = ord(i)
    if nA <= ind <= nZ:
        new_i = chr((ind + key)%(nZ+1) + ((ind + key)//(nZ+1))*nA)
        encryptor += new_i
    elif ind in range (na, nz + 1):
        new_i = chr((ind + key)%(nz+1) + ((ind + key)//(nz+1))*na)
        encryptor += new_i
    else:
        encryptor += i
print(message)
print(encryptor)
