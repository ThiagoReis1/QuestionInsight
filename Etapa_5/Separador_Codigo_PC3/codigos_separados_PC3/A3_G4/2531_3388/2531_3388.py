v = float(input())
m = float(input())
j = float(input())

cont = 0
inicial = v
saldo = v
dif = 0

if v > 0 and m > 0 and j > 0:
	while inicial < saldo:
		saldo = round((saldo + (saldo * (j/100)) - m),2)
		cont = cont + 1
		dif = saldo * 0.1 
		m = float(input())
	print(cont)
else:
	print("Dados incorretos")

	
