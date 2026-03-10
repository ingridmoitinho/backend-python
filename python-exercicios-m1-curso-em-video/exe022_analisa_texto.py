# crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiúsculas
# - o nome com todas as letras minúsculas
# - quantas letras ao todo (sem considerar os espaços)
# - quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}' .format(nome.upper()))
print('Seu nome em minúsculo é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' '))) 
print('Seu primeiro nome tem {} letras' .format(nome.find(' '))) 
# encontra o primeiro espaço e mostra a posição dele, que é a quantidade de letras do primeiro nome. 
# Se não tiver espaço, o find retorna -1, ou seja, o nome tem apenas um nome.

#ou
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))