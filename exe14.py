#Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus
# Fahrenheit.

tem = float(input("Digite a temperatura em Celcius: "))
far = ((9*tem)/5) +32
print('A temperatura de {} C corresponde a {}F'.format(tem,far))

