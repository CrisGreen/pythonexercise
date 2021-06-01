'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.'''

from random import randint
print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 30)
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
        print(f'voce jogou {jogador} e o computador {computador}. Total de {total}', end=' ')
        print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
        if tipo == 'P':
            print('VOCE VENCEU!')
            v += 1
        else:
            print('voce perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            v += 1
        else:
            print('VPCE PERDEU!')
            break
        print('Vamos jogar novamente? ')
print(f'GAME OVER! Voce venceu {v} vezes.')



