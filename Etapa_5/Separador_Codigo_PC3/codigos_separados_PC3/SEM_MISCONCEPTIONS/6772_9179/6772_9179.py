compra = float(input("valor da compra: "))
codigo = input("codigo(D/P/C1/C2): ")

if codigo == "D":
   total = compra - compra * 0.17
	print(round(total,2))
	
elif codigo == "P":
	total = compra - compra * 0.17
	print(round(total,2))
	
elif codigo == "C1":
	total = compra
	print(round(total,2))
	 
elif codigo == "C2":
	total = compra + compra * 0.8
	print(round(total,2))
	
	