# faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa

import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
# hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
# ou hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2f}' .format(hipotenusa))