preco_ab = float(input("preco da acao: "))
preco_fe = float(input("preco no FECHAMENTO: "))
perc = (preco_fe - preco_ab)*100
perc = round(perc, 2)
if perc >0:
	print("saldo positivo")
elif perc<0:
	print("saldo negativo")
elif perc == 0:
	print("sem variacao")

