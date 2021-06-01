#Faça um programa que leia a largura e a altura
#de uma parede em metros, calcule a sua área e a
#quantidade de tinta necessária para pintá-la, sabendo que
#cada litro de tinta pinta uma área de 2 metros quadrados.

lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite e altura da parede: '))
area = lar * alt
print('Sua parede tem  a dimensao de {} x {} e sua area de {}'.format(lar,alt,area))
tinta = area/2
print('Para pintar essa parede, voce precisara de {} de tinta'.format(tinta))