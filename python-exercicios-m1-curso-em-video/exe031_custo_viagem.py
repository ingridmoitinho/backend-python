# desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia = float(input('Qual é a distância da sua viagem em km? '))

""""if distancia <= 200:
    preco = distancia * 0.50
    print('Você está prestes a começar uma viagem de {}km'.format(distancia))
    print('O preço da sua passagem será de R${:.2f}' .format(preco))
else:
    preco = distancia * 0.45
    print('Você está prestes a começar uma viagem de {}km'.format(distancia))
    print('O preço da sua passagem será de R${:.2f}' .format(preco))"""

# ou maneira simplificada usando operador ternário
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
print('O preço da sua passagem será de R${:.2f}' .format(preco))