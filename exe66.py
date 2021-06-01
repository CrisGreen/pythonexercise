'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
qual foi a soma entre elas (desconsiderando o flag)'''

'''n = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
print('A soma vale {}.'.format(s))'''

cont = s =0
while True:
    n = int(input('Digite um valor, para parar digite [999]: '))
    if n == 999:
        break
    cont += 1
    s += n

print(f'A soma dos {cont} valores {s} ')


