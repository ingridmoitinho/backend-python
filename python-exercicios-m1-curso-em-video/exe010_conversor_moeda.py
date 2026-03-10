# crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1,00 = R$5,26

real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.26
print('Com R${:.2f} você pode comprar US${:.2f}' .format(real, dolar))