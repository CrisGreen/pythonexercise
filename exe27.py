'''Faça um programa que leia o nome completo de
uma pessoa, mostrando em seguida o primeiro e o
último nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).strip()
pri = nome.split()
#print(pri)
print('Seu primeiro nome e {} '.format(pri[0]))
#print('Seu ultimo nome e {}'.format(nome[len(nome)-1]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

# mesmo fazendo codigo copiado da internet
continua me apresentando o ultimo nome errado
