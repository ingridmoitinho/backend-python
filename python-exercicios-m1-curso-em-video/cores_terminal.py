# \033[0;30;41m 
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[m
# \033[7;30m

print('\033[30mEsta frase deveria estar PRETA\033[m')
print('\033[31mEsta frase deveria estar VERMELHA\033[m')
print('\033[32mEsta frase deveria estar VERDE\033[m')
print('\033[33mEsta frase deveria estar AMARELA\033[m')
print('\033[34mEsta frase deveria estar AZUL\033[m')
print('\033[35mEsta frase deveria estar ROXA\033[m')
print('\033[36mEsta frase deveria estar CIANO\033[m')
print('\033[37mEsta frase deveria estar BRANCA\033[m')

print('\033[30;41mTexto PRETO com FUNDO VERMELHO\033[m')
print('\033[33;44mTexto AMARELO com FUNDO AZUL\033[m')
print('\033[35;43mTexto ROXO com FUNDO AMARELO\033[m')
print('\033[30;42mTexto PRETO com FUNDO VERDE\033[m')

print('\033[1;31mTexto VERMELHO em NEGRITO\033[m')
print('\033[4;34mTexto AZUL SUBLINHADO\033[m')
print('\033[7;30mTexto com cores INVERTIDAS\033[m')

a = 3
b = 5
print('Os valores são \033[31m{}\033[m e \033[32m{}\033[m!!!' .format(a,b))

nome = 'Ingrid'
cores = {'limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!' .format(cores['azul'], nome, cores['azul']))

