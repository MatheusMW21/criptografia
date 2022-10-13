# criptografia :skull:
Neste repositório contém testes que serão utilizados em um projeto da faculdade sobre Criptografia em Python.

# Conceito
A criptografia envolve a conversão de texto simples legível por humanos em texto incompreensível, o que é conhecido como texto cifrado. Essencialmente, isso significa pegar dados legíveis e transformá-los de forma que pareçam aleatórios. A criptografia envolve o uso de uma chave criptográfica, um conjunto de valores matemáticos com os quais tanto o remetente quanto o destinatário concordam. O destinatário usa a chave para descriptografar os dados, transformando-os de volta em texto simples e legível.

# AES helper
O AES Helper por muito tempo foi um algoritmo de Criptografia praticamente 'indescifrável', podendo suportar chaves de 128, 192 e 256 bits, o AES utilizou de um sistema de permutações e combinações possíveis para 256 bits ou seja 2^256.
Os dados são empilhados em uma matriz 4x4 de 128 bits (16 bytes). Utilizando-se certas operações vinculadas que realizam o embaralhamento em cada estado. Sendo eles:
- Expansão de Chave e AddRoundKey;
- SubBytes;
- ShiftRows;
- MixColumns.
<img height = "200em" src = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/AES_%28Rijndael%29_Round_Function.png/250px-AES_%28Rijndael%29_Round_Function.png"/>

# Salsa20
Salsa20 é um esquema de <i>stream cripto</i> desenvolvido por Daniel J. Bernstein. É uma cifra de fulxo de 20 rodadas. A Salsa 20/20 é consistentemente mais rápida que o AES e é recomendada pelo designer para aplicações criptográficas típicas. As cifras de rodadas reduzidas, Salsa20/12 e 20/8 estão entre as cifras de fluxo de 256 bits mais rápidas e disponíveis. Comumente utilizado para aplicativos em que a velocidade é mais importante que a confiança. O algoritmo de cifragem utiliza a adição de bit a bit (xOR), adição de 32 mod 2^32 e uma distância constante de operações de rotação em um estado interno de palavras de 32 bits.
O estado inicial do algoritmo é formado por 8 palavras-chaves, sendo estas: 2 palavras de posição de fluxo, 2 palavras de <i>nonce</i> e 4 palavras constantes. Como resultado de 20 rodadas de mistura, são produzidas 16 palavras de saída da cifra de fluxo. Cada rodada de mistura consiste de 4 operaçõesde quarto-de-rodada, realizadas nas colunas ou nas linhas de estado de 16 palavras de saída da cifra de fluxo.
