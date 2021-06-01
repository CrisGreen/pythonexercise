#Escreva um programa que leia um valor em
# metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digete um valor em metros: '))
cen = metro / 0.01
mil = metro / 0.001
print('{} metros tem {} centimetros e {:.1f} milimitros'.format(metro,cen,mil))
