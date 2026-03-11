valor_compra = float(input("Digite o valor: "))
codigo = input("Digite o codigo (D, P , C1 , C2): ")

if codigo == "D":
	final = valor_compra * 0.12
elif codigo == "P":
	final = valor_compra * 0.12
elif codigo == "C1":
	final = valor_compra 
elif codigo == "C2":
	final = valor_compra * 0.07	
else:
	print(round(final, 2))