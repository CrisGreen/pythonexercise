'''Crie um programa que leia dois valores e
mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
''''n1 = int(input('Digite primeiro valor: '))
n2 = int(input('Digite segundo valor: '))
opcao = 0
while opcao != 5:
    print(
    #[ 1 ] somar
    #[ 2 ] multiplicar
    #[ 3 ] maior
    #[ 4 ] novos números
    #[ 5 ] sair do programa)
    opcao = int(input('>>>>>>>Qual e a sua opcao? '))
    if opcao ==1:
        soma = n1 + n2
        print('A soma entre {} + {} e {}.'.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 + n2
        print('O produto entre {} + {} e {}.'.format(n1, n2, produto)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Digite primeiro valor: '))
        n2 = int(input('Digite segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
print('Fim do programa! Volte sempre!')
print('=-=' * 10)
print('Fim do processo, volte sempre!')'''

from time import sleep
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    opçao = int(input('Qual sua opção? >>>> '))
    if opçao == 1:
        print(f'A soma entre {a} e {b} é {a+b}')
        print('-=-' * 20)
    elif opçao == 2:
        print(f'O produto entre {a} e {b} é {a * b}')
        print('-=-' * 20)
    elif a > b:
      maior = a
    else:
      maior = b
    if opçao == 3:
       print(f'Entre {a} e {b} o maior é {maior}')
       print('-=-' * 20)
    if opçao == 4:
      print('Informe os números novamente >>>> ')
      a = int(input('Primeiro valor: '))
      b = int(input('Segundo valor: '))
    if opçao == 5:
        print('Finalizando...')
        sleep(1)
        print('-=-' * 20)
        print('Volte sempre.')




