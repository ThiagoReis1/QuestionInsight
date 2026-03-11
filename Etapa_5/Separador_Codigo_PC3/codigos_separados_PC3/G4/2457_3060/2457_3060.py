b = int(input("Quantidade de bilhetes: "))
a = input("Acomodacao: ")

if(a == "rede"):
	v = 500.00 * b
	print(round(v, 2))
elif(a == "camarote"):
	v = 1200.00 * b
	print(round(v, 2))
elif(a == "suite"):
	v = 1500.00 * b
	print(round(v, 2))
else:
	print("acomodacao invalida")