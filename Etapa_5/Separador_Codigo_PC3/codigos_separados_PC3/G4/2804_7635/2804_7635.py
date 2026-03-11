d = int(input("deposito inicial:"))
m = int(input("numero de meses:"))

cont = 0

while(cont != m):
	cont = cont + 1
	d = d + ((d * 1 )/ 100)
	print(round(d, 2))