'''Crie um programa que leia o nome completo
de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

'''

nome = str(input('Digite seu nome completo: ')).strip() # ja elimnina os espacos antes e depois
print('Seu nome em maiscula eh {}.'.format(nome.upper()))
print('Seu nome todo em misnusculo eh {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras. '.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {}.'.format(nome.find(" ")))
separa = nome.split()
print(separa)
print('Seu primeiro nome e {} e ele tem {} letras.'.format(separa[0], len(separa[0])))