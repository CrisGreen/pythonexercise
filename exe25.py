'''Crie um programa que leia o nome de uma pessoa e diga se
ela tem “SILVA” no nome.'''

''' EU FIZ MAS NAO FUNCIONOU
nome = str(input('Digite o seu nome: ')).strip()
if nome.lower() == 'silva':
    print('Seu nome tem Silva nele')
else:
    print('Seu nome nao tem Silva nele')'''


nome = str(input('Digite o seu nome: ')).strip()
print('Seu nome tem silva {}'.format('silva' in nome.lower()))