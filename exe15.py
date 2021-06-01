#Escreva um programa que pergunte a quantidade
# de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a
# pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("Qual a quantidade de km percorrido? "))
dias = int(input("Qual a quantidade de dias alugado?"))
preco = (km * 0.15) + (dias * 60)
print(" Voce percorreu {} em {} dias e o preco total sera {}".format(km,dias,preco))