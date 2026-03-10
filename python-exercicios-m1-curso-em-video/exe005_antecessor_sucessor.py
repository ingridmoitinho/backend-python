# faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número:'))
antecessor = numero - 1
sucessor = numero + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}' .format(numero, antecessor, sucessor))

# outra forma de fazer o mesmo programa (sem criar as variáveis antecessor e sucessor)
numero = int(input('Digite um número:'))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}' .format(numero, (numero - 1), (numero + 1)))   