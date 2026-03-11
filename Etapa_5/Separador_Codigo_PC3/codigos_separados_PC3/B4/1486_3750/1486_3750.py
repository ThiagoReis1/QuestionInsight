nome = input("nome do ingrediente : ").upper()
quant = int(input(""))
if(quant < 0):
	print("Entrada invalida")
elif(quant > 10000):
	print("Entrada invalida")
elif(nome == "ARROZ"):
	print(int(quant / 500))
elif(nome == "CENOURA"):
	print(int(quant / 100))
elif(nome == "KAMPYO"):
	print(int(quant / 20))
elif(nome == "NORI"):
	print(int(quant / 50))
elif(nome == "OMELETE"):
	print(int(quant / 200))
elif(nome == "PEPINO"):
	print(int(quant / 150))
elif(nome == "SALMAO"):
	print(int(quant / 300))
elif(nome == "SHITAKE"):
	print(int(quant / 150))
else:
	print("Entrada invalida")