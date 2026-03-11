a = float(input("O preco da acao na abertura da bolsa: "))
f = float(input("O preco do fechamento da bolsa: "))

perc = f - a 
perc = round(perc,2)
if(perc>0):
	print("saldo positivo")
elif(perc == 0):
	print("sem variacao")
else:
	print("saldo negativo")