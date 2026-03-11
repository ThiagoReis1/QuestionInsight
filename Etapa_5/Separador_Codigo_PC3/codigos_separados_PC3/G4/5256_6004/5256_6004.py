pa = float(input("preco da acao na abertura da bolsa: "))
pf = float(input("preco da acao no fechamento da bolsa: "))

if (pf>pa and pf>0):
	print("saldo positivo")
elif (pa==pf):
	print("sem variacao")
else:
	print("saldo negativo")