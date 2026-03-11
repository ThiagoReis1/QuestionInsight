#Trabalho Prático 1
#Ex 01
#03/11/2016

carros = float(input("Insira a estimativa de carros: "))
a = float(input("Insira o comprimento do cateto a: "))
b = float(input("Insira o comprimento do cateto b: "))

area = a * b / 2

total = carros * (a * b / 2) #número total de carros

print(int(round(total, 2)))