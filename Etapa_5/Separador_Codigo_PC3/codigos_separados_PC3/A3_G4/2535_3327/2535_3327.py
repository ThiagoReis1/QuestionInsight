DA = int(input("Valor depositado A: "))
DB = int(input("Valor depositado B: "))
jA = float(input("Taxa de juros A: "))
jB = float(input("Taxa de juros B: "))

t = 0
saldo = 0     # Variavel acumuladora

while (t > 0):
	saldo = (DA * jA)
	saldo = saldo + DA
	saldo = (DB * jB)
	saldo = saldo + DB
	
	print(round(saldo, 2))
	t = t + 1