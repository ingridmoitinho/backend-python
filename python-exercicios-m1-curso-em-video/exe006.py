# crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um número:'))
print('O dobro de {} vale {}. \n' 
'O triplo de {} vale {}. \n' 
'A raiz quadrada de {} é igual a {:.2f}' .format(numero, (numero * 2), numero, (numero * 3), numero, (numero ** (1/2))))
#'A raiz quadrada de {} é igual a {:.2f}' .format(numero, (numero * 2), numero, (numero * 3), numero, pow(numero, 1/2)))

# outra forma de fazer usando variáveis para armazenar o dobro, triplo e raiz quadrada
numero = int(input('Digite um número:'))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** (1/2)
print('O dobro de {} vale {}' .format(numero, dobro))
print('O triplo de {} vale {}' .format(numero, triplo)) 
print('A raiz quadrada de {} é igual a {:.2f}' .format(numero, raiz_quadrada))