x = float(input("preco da acao na abertura da bolsa: "))
y = float(input("preco da acao no fechamento da bolsa: "))

zav = round(y - x, 2)

if zav > 0:
	print("saldo positivo")
elif zav == 0:
	print("sem variacao")
else:
	print("saldo negativo")