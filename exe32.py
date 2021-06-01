'''Faça um programa que leia um ano qualquer e
mostre se ele é bissexto.
Anos bissextos são aqueles que são múltiplos de 4,
como 1996, 2000, 2004 etc (que podem ser divididos por 4
deixando resto 0). Porém, há uma exceção:
múltiplos de 100 que não sejam múltiplos de 400.'''

from datetime import date
ano = int(input('Que ano voce quer analizar? Coloque 0 para analizar o dia atual'))
if ano ==0:
    ano =date.today().year
if ano %4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} e bisexto'.format(ano))
else:
    print('O ano {} nao eh bisexto'.format(ano))