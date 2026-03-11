x = input("unidade(K/O)")

if(x == "O"):
	O = float(input("valor: "))
	kg = O/35.274
	print(round(kg , 2))
else:
	kg = float(input("valor: "))
	O = 35.274 * kg
	print(round(O,2))