#Universidade Federal do Amazonas
#Marcos Stephano Maia de Lima - 21602344

from math import*
A = float(input("compra a: "))
B = float(input("compra b: "))
C = float(input("compra c: "))
LC = int(input("Limite do cartao: "))

if((A + B + C) < LC):
	print("sim")
else:
	print("Nao")
print(round(LC, 2))