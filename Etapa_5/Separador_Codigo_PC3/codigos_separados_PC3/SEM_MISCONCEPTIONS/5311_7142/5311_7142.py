d = float(input())
m = int(input())
juros = 0.012
saldo = d
cont = 0 

while(cont < m):
	rend = saldo * juros 
	saldo = saldo + rend
	cont = cont + 1
	print(round(saldo, 2))