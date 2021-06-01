lanche = ('Hambuerger', 'Suco', 'Pizza', 'Pudim', 'Bata Frita')

for comida in lanche:
    print(f'Eu vou comer {comida} ')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posico {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posicao {pos}')

print('Comi pra caramba! ')
