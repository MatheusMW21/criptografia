# criptografia :skull:
Neste repositório contém testes que serão utilizados em um projeto da faculdade sobre Criptografia em Python.

# Conceito
A criptografia envolve a conversão de texto simples legível por humanos em texto incompreensível, o que é conhecido como texto cifrado. Essencialmente, isso significa pegar dados legíveis e transformá-los de forma que pareçam aleatórios. A criptografia envolve o uso de uma chave criptográfica, um conjunto de valores matemáticos com os quais tanto o remetente quanto o destinatário concordam. O destinatário usa a chave para descriptografar os dados, transformando-os de volta em texto simples e legível.

# Cifra de César
Primordialmente, na Idade Antiga, a Cifra de César, conhecida também como Troca de César, Cifra de Troca ou Código de César, foi usada pelo próprio Júlio César como forma de codificar suas mensagens enviadas para seus Generais de Guerra, com a finalidade de esconder informações de tropas inimigas. Ficou conhecida como um sistema de criptografia simples, usando a técnica de substituição. Consiste na substituição da letra por 3 posições à frente, por exemplo, a substiuição de A seria D, de B seria E e assim sucessivamente.<br><br>
<img  height = "200em" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Caesar3.svg/320px-Caesar3.svg.png">

# AES helper
O AES Helper por muito tempo foi um algoritmo de Criptografia praticamente 'indescifrável', podendo suportar chaves de 128, 192 e 256 bits, o AES utilizou de um sistema de permutações e combinações possíveis para 256 bits ou seja 2^256.
Os dados são empilhados em uma matriz 4x4 de 128 bits (16 bytes). Utilizando-se certas operações vinculadas que realizam o embaralhamento em cada estado. Sendo eles:
- Expansão de Chave e AddRoundKey;
- SubBytes;
- ShiftRows;
- MixColumns.
<img height = "200em" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/AES_%28Rijndael%29_Round_Function.png/250px-AES_%28Rijndael%29_Round_Function.png"/>

# Salsa20
Salsa20 é um esquema de <i>stream cripto</i> desenvolvido por Daniel J. Bernstein. É uma cifra de fluxo de 20 rodadas. A Salsa 20/20 é consistentemente mais rápida que o AES e é recomendada pelo designer para aplicações criptográficas típicas. As cifras de rodadas reduzidas, Salsa20/12 e 20/8 estão entre as cifras de fluxo de 256 bits mais rápidas e disponíveis. Comumente utilizado para aplicativos em que a velocidade é mais importante que a confiança. O algoritmo de cifragem utiliza a adição de bit a bit (xOR), adição de 32 mod 2^32 e uma distância constante de operações de rotação em um estado interno de palavras de 32 bits.
O estado inicial do algoritmo é formado por 8 palavras-chaves, sendo estas: 2 palavras de posição de fluxo, 2 palavras de <i>nonce</i> e 4 palavras constantes. Como resultado de 20 rodadas de mistura, são produzidas 16 palavras de saída da cifra de fluxo. Cada rodada de mistura consiste de 4 operaçõesde quarto-de-rodada, realizadas nas colunas ou nas linhas de estado de 16 palavras de saída da cifra de fluxo.

# ChaCha20
ChaCha20-Poly1305 é um <i>autheticated encryption with addtional data</i>(AEAD) algoritmo, que combina o ChaCha20 com a stream cipher Poly1305 código de autenticação de mensagem. São algoritmos criptográficos projetado por Daniel J.Bernstein com o objetivo de garantir segurança extrema e que ao mesmo tempo atinja uma alta performance em uma variedade de plataformas de softwares.
Em resposta às preocupações levantadas sobre a confiabilidade do conjunto dfe cifras IETF/TLS existente, seu alto desempenho em plataformas de softwares e a facilidade de realizar implementações seguras, o IETF publicou recentemente novos protocolos para promover o uso e padronização do stream cipher ChaCha20 e o autenticador Poly1305 no protocolo TLS.

<img height = 200em src = "https://javainterviewpoint.com/wp-content/uploads/2019/04/Java-ChaCha20-Poly1305-Encryption-and-Decryption-Example.png"/>

O código de autenticação de mensagem Poly1305 garante:
- Verficação de integridade 
- Autenticidade dos dados
Uma característica muito importante do ChaCha20 frente ao AES é custo computacional baixo para dispositivos móveis ou com baixa disponibilidade energética, sendo 5 vezes mais eficiente neste quesito se comparando ao AES.

# RSA
O RSA é um dos primeiros sistemas de criptografia que utilizam de chaves públicas. E nesse caso, a chave de criptografia é diferente a decriptografia que é uma chave privada. No RSA, esta assimetria é baseada na dificuldade prática da fatorização do produto de dois números primos grandes, o "problema de fatoração".
- Geração de chaves:
1 . Escolha de forma aleatória dois números primos grandes p e q, da ordem 10^100 no mínimo
2 . Calcule n = pq
3 . Calcule a Função totiente de Euler n: phi(n) = (p-1)(q-1)
4 . Escolha um número inteiro e tal que 1 < e < phi(n) sejam relativamente primos entre si
5 . Calcule d de forma que d == 1 (mod phi(n))
- Por final temos: 
A chave pública: o par (n, e)
A chave privada: a tripla (p, q, d)

- Encriptação:
<img height = 30em src = "https://wikimedia.org/api/rest_v1/media/math/render/svg/e50dd9804137b10a7854b48934c5b920ef26b78b">

- Decriptação:
<img height = 30em src = "https://wikimedia.org/api/rest_v1/media/math/render/svg/1d2604ec76ac085c320956536de0b16f6a6f59af">
