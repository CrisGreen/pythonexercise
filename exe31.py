'''Desenvolva um programa que pergunte a distância
 de uma viagem em Km. Calcule o preço da passagem,
 cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distanciaa = float(input('Qual a distancia da viagem em km?'))
if distanciaa <=200:
    preco = distanciaa * 0.50
else:
    preco = distanciaa * 0.45
print('e o preco da sua passagem sera {:.2f}'.format(preco))