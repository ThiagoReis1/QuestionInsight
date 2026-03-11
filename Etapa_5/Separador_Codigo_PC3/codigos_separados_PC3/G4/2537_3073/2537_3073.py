from math import * 
v = float(input("Valor da heranca:")) 
m = float(input("Saque mensal:")) 
j = float(input("Taxa de juros:")) 

pj = j / 100
i = 0
saldo = v

if ((v >0) and (m >0)):
	while (saldo < (v + (20 /100) * v)):
		saldo = saldo + (saldo * pj) - m
		round(saldo, 2)
		i = i + 1
	print(i)
else:
	print("Dados incorretos")	