#usando for
mensagem = [65, 99, 104, 111, 117, 33]
for i in mensagem: 
    print('{0} = {1}'.format(i, chr(i)))
for i in mensagem:
    print(chr(i),end ='')