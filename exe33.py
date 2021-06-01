'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

a = int(input('Digite primeiro numero: '))
b = int(input('Digite segundo numero: '))
c = int(input('Digite terceiro numero: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}.'.format(maior))
