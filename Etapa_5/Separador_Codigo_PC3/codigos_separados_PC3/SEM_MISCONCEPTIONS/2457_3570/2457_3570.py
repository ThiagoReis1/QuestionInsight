q = int(input("quantidade:"))
a = input("tipo de acomodacao (rede, camarote ou suite):")

if (a == "rede"):
	valor = q*500
	print(round(valor,2))
elif (a == "camarote"):
	valor = q*1200
	print(round(valor,2))
elif (a == "suite"):
	valor = q*1500
	print(round(valor,2))
else:
	print("acomodacao invalida")