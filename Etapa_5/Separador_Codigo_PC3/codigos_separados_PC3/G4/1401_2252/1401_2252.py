at = input("informe o tipo de ataque usado:")
qtde = int(input("informe a quantidade de baforadas:"))
q1 = 40
q2 = 150
if (at != "maritimo"):
	print("Drogon")
	print(int(qtde * q2))
else:
	print("Viserion")
	print(int(qtde * q1))