V = float(input("heranca: "))
M = int(input("saque mensal: "))
j = float(input("taxa de juros: "))
saldo = V
t = 0
if (V > 0) and (M > 0) and (j > 0):
	while (saldo <= 1.20*V):
		saldo = saldo + saldo * (j/100)
		saldo = round(saldo,2)
		saldo = saldo - M
		t = t + 1
	print(t)
else:
	print("Dados invalidos")