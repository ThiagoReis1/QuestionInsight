cond = input("Qual o tipo de ataque maritimo/terrestre: ")
baf = int(input("Informe o número de baforadas: "))
viserion = baf//40
drogon = baf//150
if (cond.lower() == "maritimo"):
	print("Viserion")
	print(viserion + 1)
if (cond.lower() == "terrestre"):
	print("Drogon")
	print(drogon + 1)