# escreva um programa que converta uma temperatura digitada em °C e converta para °F

c = float(input('Informe a temperatura em °C:'))
f = c * 9 / 5 + 32 # não precisa de () porque a ordem de precedência já é multiplicação e divisão antes de adição
# ou f = (c * 9 / 5) + 32
print('A temperatura de {:.1f}°C corresponde a {:.1f}°F!'.format(c, f))