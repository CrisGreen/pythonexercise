'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''

total = totmil = menor = cont = 0
while True:
    produto = str(input('Qual o nome do produto?'))
    preco = float(input('Preco: R$'))
    cont += 1
    total += preco
    if preco >= 1000:
        totmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Fim do programa'))
print(f'O total da compra foi {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000 reais. ')
print(f'O produto mais barato custa R${menor:.2f}')
