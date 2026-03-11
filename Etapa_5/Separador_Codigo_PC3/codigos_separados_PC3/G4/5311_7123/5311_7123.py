di = float(input("digite o deposito inicial:"))
n = int(input("digite o numero de meses:"))
cont = 0
total = di

while (cont < n):
	total = total + (total * 1.2/100)
	cont = cont + 1
	print(round(total,2))