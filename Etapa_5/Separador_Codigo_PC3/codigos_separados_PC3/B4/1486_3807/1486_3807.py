nome = input("digite:")
quant = int(input("digite:"))

if (quant < 0 or quant > 10000):
	a = "Entrada invalida"
	print (a)
elif (nome == "ARROZ"):
	a = quant//500
	print(a)
	
elif (nome == "CENOURA"):
	a = quant//100
	print(a)
	
elif (nome == "KAMPYO"):
	a = quant//20
	print(a)
	
elif (nome == "NORI"):
	a = quant//50
	print(a)
	
elif (nome == "OMELETE"):
	a = quant//200
	print(a)
	
elif (nome == "PEPINO"):
	a = quant//150
	print(a)
	
elif (nome == "SALMAO"):
	a = quant//300
	print(a)
	
elif (nome == "SHITAKE"):
	a = quant//150
	print(a)
	
else:
	print("Entrada invalida")