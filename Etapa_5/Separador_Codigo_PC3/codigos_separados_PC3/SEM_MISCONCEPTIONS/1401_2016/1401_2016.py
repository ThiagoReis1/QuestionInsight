dragao = input("Digite o tipo de ataque: ")
quantidade = int(input("Digite quantidade de unidades destruidas: "))
viserion = quantidade//40+1
drogon = quantidade//150+1
if dragao=='maritimo':
	print("Viserion", viserion)
else:
	print("Drogon", drogon)