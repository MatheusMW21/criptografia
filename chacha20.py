import chilkat  
#Neste algoritmo a API do Chilkat deve estar instalada no computador

crypt = chilkat.CkCrypt2()

#Coloque o algoritmo para rodar em chacha20
crypt.put_CryptAlgorithm('chacha20')

#O tamanho da chave do chacha20 sempre será 256 bits
crypt.putKeyLenght(256)

#Sendo chacha20 uma stream cipher, não exite um padding específico
# e o output será o número de bytes exatamente igual ao input

#O EncondingMode especifica o tipo de criptografia e a entrada da descriptografia
crypt.put_EncondingMode('hex')

ivHex = '000000000000000000000002'
crypt.SetEncodedIV(ivHex, 'hex')

crypt.put_InitialCount(42)

keyHex = '1c9240a5eb55d38af333888604f6b5f0473917c1402b80099dca5cbc207075c0'
crypt.SetEncodeKey(keyHex, 'hex')

plainText = 'Twas brillig, and the slithy toves\nDid gyre and gimble in the wabe:\nAll mimsy were the borogoves,\nAnd the mome raths outgrabe.'

#criptografando
encStr = crypt.encryptStringENC(plainText)
print(encStr)

#descriptografando
decStr = crypt.decryptStringENC(encStr)
print(encStr)

#TESTES

#  Key:
#  000  1c 92 40 a5 eb 55 d3 8a f3 33 88 86 04 f6 b5 f0  ..@..U...3......
#  016  47 39 17 c1 40 2b 80 09 9d ca 5c bc 20 70 75 c0  G9..@+....\. pu.
# 
#  Nonce:
#  000  00 00 00 00 00 00 00 00 00 00 00 02              ............
# 
#  Initial Block Counter = 42
# 
#  Plaintext:
#  000  27 54 77 61 73 20 62 72 69 6c 6c 69 67 2c 20 61  'Twas brillig, a
#  016  6e 64 20 74 68 65 20 73 6c 69 74 68 79 20 74 6f  nd the slithy to
#  032  76 65 73 0a 44 69 64 20 67 79 72 65 20 61 6e 64  ves.Did gyre and
#  048  20 67 69 6d 62 6c 65 20 69 6e 20 74 68 65 20 77   gimble in the w
#  064  61 62 65 3a 0a 41 6c 6c 20 6d 69 6d 73 79 20 77  abe:.All mimsy w
#  080  65 72 65 20 74 68 65 20 62 6f 72 6f 67 6f 76 65  ere the borogove
#  096  73 2c 0a 41 6e 64 20 74 68 65 20 6d 6f 6d 65 20  s,.And the mome
#  112  72 61 74 68 73 20 6f 75 74 67 72 61 62 65 2e     raths outgrabe.
# 
#  Ciphertext:
#  000  62 e6 34 7f 95 ed 87 a4 5f fa e7 42 6f 27 a1 df  b.4....._..Bo'..
#  016  5f b6 91 10 04 4c 0d 73 11 8e ff a9 5b 01 e5 cf  _....L.s....[...
#  032  16 6d 3d f2 d7 21 ca f9 b2 1e 5f b1 4c 61 68 71  .m=..!...._.Lahq
#  048  fd 84 c5 4f 9d 65 b2 83 19 6c 7f e4 f6 05 53 eb  ...O.e...l....S.
#  064  f3 9c 64 02 c4 22 34 e3 2a 35 6b 3e 76 43 12 a6  ..d.."4.*5k>vC..
#  080  1a 55 32 05 57 16 ea d6 96 25 68 f8 7d 3f 3f 77  .U2.W....%h.}??w
#  096  04 c6 a8 d1 bc d1 bf 4d 50 d6 15 4b 6d a7 31 b1  .......MP..Km.1.
#  112  87 b5 8d fd 72 8a fa 36 75 7a 79 7a c1 88 d1     ....r..6uzyz..
