DA=float(input("Valor do deposito A: "))
DB=float(input("Valor do deposito B: "))
jA=float(input("Juros no banco A: "))
jB=float(input("Juros no banco B: "))
saldoA = DA
saldoB = DB
i = 0
jA = jA/100
jB = jB/100

if (DA>0 and DB>0 and jA>0 and jB>0):
	while (DA > DB and jA < jB):
		saldoA = round(saldoA + (saldoA*jA) + DA,2)	
		saldoB = round(saldoB + (saldoB*jB) + DB,2)
		i = i + 1
		print(i)
	
else:
	print("Dados incorretos")