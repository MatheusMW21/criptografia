import os, base64, random;

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class AesHelper():
    def __init__(self, key=None, iv=None): #define como parâmetro ele mesmo, a chave e seu vetor de inicialização (iv)
        if key == None:
            self.key = os.urandom(32) #caso não for definido a chave, ela será uma chave randomica 32 bits
        else:
            self.key = key #senão ela recebe a chave fornecida pelo usuário
        if iv == None:
            self.iv = os.urandom(16)  #recebe chave random de 16 bits
        else:
            self.iv = iv
        self.cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv) )
#Criptografia 
    def encrypt (self, message):
        message = base64.b64encode(message.encode()).decode()
        for i in range (16 -len(message) % 16):
            message += " "
        encryptor = self.cipher.encryptor()
        return encryptor.update(message.encode('utf-8')) + encryptor.finalize()
#Descriptografia
    def decrypt(self, message):
        decryptor = self.cipher.decryptor()
        return base64.b64decode( (decryptor.update(message) + decryptor.finalize()).decode("utf-8") ).decode("utf-8")   

if __name__ == "__main__":
	ae = AesHelper()
	criptografado = ae.encrypt(input("Digite o texto a ser criptografado: "))
	print(criptografado)
	print(ae.decrypt(criptografado))