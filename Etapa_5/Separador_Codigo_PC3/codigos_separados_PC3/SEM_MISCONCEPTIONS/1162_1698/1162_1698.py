lot = float(input("Quanto ele recebeu na loteria: "))
taxa = float(input("Taxa de rendimento: "))
gastos = float(input("Gasto mensal: "))
t = 0
saldo = lot
mes = gastos

while ( gastos < saldo ):
	investido = lot * taxa
	saldo = lot + investido 
	t = t + 1
	gastos = mes + gastos
print(t)