#usando while ASCII 
mensagem = [65, 99, 104, 111, 117, 33]
i = 0
while i < len(mensagem):
    print('{0} = {1}'.format(mensagem[i], chr(mensagem[i])))
    i+=1
while i < len(mensagem):
    print(chr(mensagem[i], end = ''))
    i += 1