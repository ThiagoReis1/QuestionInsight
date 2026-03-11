abe = float(input("preco na abertura: ")) 
fec = float(input("preco no fechamento: "))

if fec > abe:
	print("saldo positivo")
	
elif fec < abe:
	print("saldo negativo")
	
elif fec == abe:
	print("sem variacao")