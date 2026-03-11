from math import *
d = float(input("Deposito inicial: "))
tf = float(input("Tarifa mensal: "))
j = float(input("Juros: "))
pj = j / 100
i = 0
saldo = d 

if ((d > 0) and (tf > 0) and (j > 0)):
	while(saldo < (d + (15/100) * d)):
		saldo = saldo + (saldo * pj) - tf
		round(saldo, 2)
		i = i + 1
	print(i)
else:
	print("Dados incorretos")