#Faça um algoritmo que leia o salário de um f
# uncionário e mostre seu novo salário, com 15% de aumento.

sal = float(input("Digite o seu salario: "))
novo = sal + (sal *15/ 100)
print(" o seu salario era {} e agora com o novo aumento sera {}".format(sal,novo))