#Faça um programa que leia algo pelo teclado e
# mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

algo=input('Digite algo: ')
print('O tipo primitivo desse valor e ',type(algo))
print('So tem espaco?', algo.isspace())
print('E um numero?', algo.isnumeric())
print('E afabetico? ', algo.isalnum())
print('Esta em maisculas?', algo.isupper())
print('Esta em minusculas? ', algo.islower())
print('sEta em alfanumerico? ', algo.isprintable())
print('Esta capitalizada? ', algo.istitle())

