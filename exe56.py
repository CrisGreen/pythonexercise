'''Desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas. No final do programa, mostre: a média de
idade do grupo, qual é o nome
do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaiade = 0
mediaidade = 0
maioridadedehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('------ {} PESSO ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    somaiade =+ idade
    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaiade / 4
print('A media de idade do grupo e de {} anos'.format(mediaidade))
print(" O homem mais velho tem {} anos e se chama {}".format(maioridadedehomem,nomevelho))
print('Ao todo sao {} mulheres com menos de 20 anos.'.format(totmulher20))

#a soma total deu errada