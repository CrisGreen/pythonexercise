#Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira e mostre quantos dólares ela pode comprar.

din = float(input('Quanto de dinheiro voce tem na carteira? R$'))
print('Voce com {} reais pode comprar US{:.2f} dolares.'.format(din,din /5.75))