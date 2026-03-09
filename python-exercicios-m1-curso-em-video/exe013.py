# faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 0.15)
# ou aumento = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com o aumento de 15% vai ganhar R${:.2f}' .format(salario, aumento))   