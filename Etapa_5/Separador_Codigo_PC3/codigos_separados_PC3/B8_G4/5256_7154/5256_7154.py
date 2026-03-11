pa = float(input("preco de abertura: "))
pf = float(input("preo de fechamento: "))

pg = pf - pa

if (pg > 0):
	print("saldo positivo")
elif(pg < 0):
	print("saldo negativo")
elif(pg == 0):
	print("sem variacao")