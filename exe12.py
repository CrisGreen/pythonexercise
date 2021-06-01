#Faça um algoritmo que leia o preço de
# um produto e mostre seu novo preço, com 5% de desconto.

prod = float(input('Qual o preco do produto? '))
desconto = prod - (prod * 5 / 100)
print('O preco do seu produto e {} e com 5% de desconto custara {}'.format(prod,desconto))