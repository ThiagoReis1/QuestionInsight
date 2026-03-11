from numpy import *

prod = input("produtos: ").upper() 

ind = 0
custo = 0

while ind < len(prod):
	if prod [ind] == "D":
		custo = custo + 2.25
	elif prod[ind] == "S":
		custo = custo + 4.00
	elif prod[ind] == "I":
		custo = custo + 6.90
	ind = ind + 1

print(round(custo,2))