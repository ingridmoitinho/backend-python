numero1 = int(input('Digite um número:'))
numero2 = int(input('Digite mais um número:'))
soma = numero1 + numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2
pontencia = numero1 ** numero2

print ('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(soma, multiplicacao, divisao), end=' ')
print('A divisão inteira é {} e a potência é {}' .format(divisao_inteira, pontencia))