from math import*
DA = float(input("Valor depositado no banco A"))
DB = float(input("Valor depositado no banco B"))
jA = float(input("Valor depositado no banco A"))/100
jB = float(input("Valor depositado no banco A"))/100

if(DA <= 0 or DB <= 0 or jA <= 0 or jB <= 0 or DA <= DB or jA >= jB):
	print("Dados incorretos")
else:
	Meses = 0
	SaldoA = DA
	SaldoB = DB

	while(SaldoB <= SaldoA):
		SaldoA += SaldoA*jA
		SaldoB += SaldoB*jB
		SaldoA = round(SaldoA,2)
		SaldoB = round(SaldoB,2)
		Meses += 1
	print(Meses)
