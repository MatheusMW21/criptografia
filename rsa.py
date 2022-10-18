'''
é aleatoriamente selecionado 2 números primos de um arquivo txt de
números e utilizados para gerar as chaves públicas e privadas
'''

import random
from math import gcd

def gcd (a, b): #mdc (máximo divisor comum)
    #Essa função roda o Euclidean Algorithm e retorna o mdc de 'a' e 'b'

    if (b == 0 ):
        return a 
    else:
        return gcd(b, a % b)

def xgcd(a, b):
    #Essa função retorna o mdc, o coeficiente de a, e o coeficiente de b
    
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y

def chooseE(totient):
    #Função Tociente de Euler
    #Escolhe um número aleatório entre 1 < e < totient
 while (True):
        e = random.randrange(2, totient)

        if (gcd(e, totient) == 1):
            return e

def chooseKeys ():

    # Escolhe 2 números primos aleatórios de uma lista de números primos que vão até 100k
    # Cria um arquivo txt e guarda 2 números primos que podem ser usados depois

    rand1 = int(input('Entre uma chave prima 1: '))
    rand2 = int(input('Entre uma chave prima 2: '))

    #guarde os números primos nessas variáveis
    prime1 = int(rand1)
    prime2 = int(rand2)

    # computa n, tociente, e
    n = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)
    e = chooseE(totient)
    # computa d, 1 < d < totient ~
    #E e D são inversos, ou seja, mod totiente

    gcd, x, y = xgcd(e, totient)

    #verifique se d é positivo
    if (x < 0):
        d = x + totient
    else:
        d = x

    #escreva as chaves publicas n e e em um arquivo
    f_public = open('public_keys.txt', 'w')
    f_public.write = (str(n) + '\n')
    f_public.write = (str(d) + '\n')
    f_public.close()

    f_private = open('private_keys.txt', 'w')
    f_private.write = (str(n) + '\n')
    f_private.write = (str(d) + '\n')
    f_private.close()

#criptografia
def encrypt(message, file_name = 'public_keys.txt', block_size = 2):
    #criptografa uma mensagem (string) elevando cada caractere ASCII pelo valor de 'e'
    #e pegando os módulos de n. 
    try:
        fo = open(file_name, 'r')
    #checa a possibilidade que o usuário tenta criptografar algo 
    #usando uma chave pública desconhecida
    except FileNotFoundError:
        print('Esse arquivo não foi encontrado')
    else:
        n = int(fo.readline())
        e = int(fo.readline())
        fo.close()

        encrypted_blocks = []
        ciphertext = -1

        if (len(message) > 0):
            #inicializa o criptografia baseada na tabela ASCII
            ciphertext = ord(message[0])

        for i in range(1, len(message)):
            if(i % block_size == 0):
                encrypted_blocks.append(ciphertext)
                ciphertext = 0

            #multiplica por 1000 para deslocar os dígitos para a esquerda em 3 casas
            #por causa dos códigos em ASCII que são no máximo 3 dígitos no decimal
            ciphertext = ciphertext * 1000 + ord(message[i])

        #adiciona o último bloco à lista
        encrypted_blocks.append(ciphertext)

        #criptografa todos os números elevando a potência de e e módulo de n
        for i in range(len(encrypted_blocks)):
            encrypted_blocks[i] = str((encrypted_blocks[i]**e)%n)
        #cria uma string de números
        encrypted_message = " ".join(encrypted_blocks)

        return encrypted_message

def main():
    choose_again = input('Você deseja gerar novas chaves públicas e privadas? (s ou n) ')
    if (choose_again == 's'):
        chooseKeys()
        message = input('O que você desejaria criptografar?\n')
        print(encrypt(message))
main()