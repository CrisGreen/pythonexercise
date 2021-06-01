'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
Para construir um triângulo não podemos utilizar qualquer medida, tem que seguir a condição de existência: Para construir
um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e
maior que o valor absoluto da diferença entre essas medidas'''
print('=' * 20)
print('Analizador de triangulos')
print('=' * 20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segudno seguimento'))
r3 = float(input('Terceiro seguimento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM formar um triangulo!')


