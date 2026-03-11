d= float(input("Digite o deposito inicial: "))
tm= float(input("Digite a tarifa mensal: "))
j= float(input("Digite a taxa de juros: "))

saldo= d
cont= 0
s= d + (d * (15 / 100))

if(d > 0) and (tm > 0) and (j > 0):
	while(saldo < s):
		saldo= saldo + (saldo * (j/100)) - tm
		round(saldo, 2)
		cont= cont + 1
	print(cont)
else:
	print("Dados incorretos")