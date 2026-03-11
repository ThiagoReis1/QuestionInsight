valor_compra = float(input("digite o valor: "))
codigo = input("digite o codigo (D, P, C1, C2): ")

if codigo == "D":
	valor_final = valor_compra * 0.17
elif codigo == "P":
	valor_final = valor_compra * 0.17
elif codigo == "C1":
	valor_final = valor_compra
elif codigo == "C2":
	valor_final = valor_compra * 0.08

print(round(valor_final,2))