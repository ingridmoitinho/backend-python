# faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
# ex: Ana Maria Silva. Primeiro nome: Ana. Último nome: Silva.

nome = str(input('Digite seu nome completo: ')).strip()
nome_separado = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}' .format(nome_separado[0]))
print('Seu último nome é {}' .format(nome_separado[len(nome_separado)-1]))
