p=float(input("abertura da bolsa: "))
f=float(input("fechamento da bolsa: "))
pg=("f - p")
if(f > 0):
	pg
	print("saldo positivo")
	print(round(p, 2))
elif(p == 0):
	print("sem variacao")
	print(round(p, 2))
elif(p <= 0):
	print("saldo negativo")
	print(round(p, 2))

	