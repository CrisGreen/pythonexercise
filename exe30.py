'''Crie um programa que leia
um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

num = int(input('Digite um numero: '))
resultado = num % 2
if resultado == 0:
    print('O numero {} e PAR'.format(resultado))
else:
    print('O numero {} e IMPAR'.format(resultado))