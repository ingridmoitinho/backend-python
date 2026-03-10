# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# ex: Digite um número: 1834. Unidade: 4. Dezena: 3. Centena: 8. Milhar: 1.

# numero = int(input('Digite um número: '))
# numero_str = str(numero)
# print('Analisando o número {}'.format(numero))
# print('Unidade: {}'.format(numero_str[3]))
# print('Dezena: {}'.format(numero_str[2]))
# print('Centena: {}'.format(numero_str[1]))
# print('Milhar: {}'.format(numero_str[0]))

numero = int(input('Digite um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))