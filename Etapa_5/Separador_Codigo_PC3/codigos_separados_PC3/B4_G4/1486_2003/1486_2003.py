x = input("Insira o nome do ingrediente: ") .upper()
y = int(input("Insira a quantidade do ingrediente: "))

if y < 0 or y > 10000:
	print("Entrada invalida")
elif(x == "ARROZ"):
	print(y // 500)
elif(x == "CENOURA"):
	print(y // 100)
elif(x == "KAMPAYO"):
	print(y // 20)
elif(x == "NORI"):
	print(y // 50)
elif(x == "OMELETE"):
	print(y // 200)
elif(x == "PEPINO"):
	print(y // 150)
elif(x == "SALMAO"):
	print(y // 300)
elif(x == "SHITAKE"):
	print(y // 150)
else:
	print("Entrada invalida")