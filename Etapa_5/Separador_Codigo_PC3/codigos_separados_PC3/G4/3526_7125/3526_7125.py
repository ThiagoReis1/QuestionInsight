var1 = float(input("num real"))
var2 = int (input("termos"))

cont = 0
aux = 1
aux1 = 1
x = 0

while cont < var2:
	cont = cont + 1
	x = x + ((var1 ** aux)/aux1)
	aux = aux + 2
	aux1 = aux1 + 2

print(round(x,7))