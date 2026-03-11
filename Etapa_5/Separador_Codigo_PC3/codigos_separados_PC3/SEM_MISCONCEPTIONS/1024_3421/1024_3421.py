from math import*
a=float(input("comprimento do terreno a: "))
b=float(input("cpmprimento do terreno b: "))
c=float(input("comprimento do terreno c: "))
custo=float(input("valor do custo: "))

p= a + b + c
valor= (p*custo)

print(round(valor, 2))

