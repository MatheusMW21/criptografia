import random

def determinaOpcao():
    #Função que pergunta c ou d, e garante loop

    while True:
        opcao = (input('Deseja criptografar ou decriptografar? (c-d)\n')).lower()
        if opcao in 'criptografar c decriptografar d'.split():
            return opcao
        else:
            print("Digite 'c' ou 'd'.")
def determinaChave():

def determinaChave():

    chave = random.randint(1, 26)
    while True:
        if 1<= chave <= 26:
            return chave

def determinaMensagem(opcao, mensagem, chave):
    
    #Confere a opção do usuário
    traduzido = ''
    if opcao[0] == 'd':
        chave *= -1

    #Criptografia e Decriptografia
    for letra in mensagem:
        if  letra.isalpha():
            num = ord(letra) #ASCII
            num += chave
            if letra.isupper():
                if num > ord ('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif letra.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traduzido += chr(num)
        else:
            traduzido += letra
    return traduzido

def main():

    opcao = determinaOpcao()
    mensagem = input('Entre com sua mensagem \n')
    chave = determinaChave()
    print('Sua frase traduzida é: ')
    print(determinaMensagem(opcao, mensagem, chave))
main()
