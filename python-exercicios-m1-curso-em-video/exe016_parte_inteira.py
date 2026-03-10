# Cria um programa que leia um numero Real qualquer pelo teclado a mostre na tela a sua porção inteira.
# Ex:
# Digite um número: 6.127. O número 6.127 tem a parte Inteira 6.

from math import trunc

numero = float(input('Digite um número:'))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(numero, trunc(numero)))

# ou

numero = float(input('Digite um número:'))
print('O valor digitado foi {} e a sua porção inteira é {}' .format(numero, int(numero)))