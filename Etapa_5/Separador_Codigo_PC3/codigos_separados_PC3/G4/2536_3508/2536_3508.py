C = float(input("Valor da casa: "))
D = float(input("Valor do deposito: "))
M = float(input("Valor mensal: "))
j = float(input("juros: "))
j = j / 100
mes = 0
saldo = 1
if ((C > 0) or (D > 0) or (M > 0) or (j > 0)):
	while(saldo < C):
		saldo = D + (j * saldo)
		saldo = saldo + M
		mes = mes + 1
else:
	print("Dados incorretos")

print(round(mes, 2))
		