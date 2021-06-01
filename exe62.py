'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input("Primeiro termo: "))
razao = int(input('Razao PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantoa termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrando'.format(total))
