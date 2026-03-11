ingrediente = input()
quantidade = int(input())
if((quantidade >= 0) and (quantidade <= 10000)):
	if(ingrediente == "ARROZ"):
		valor = (quantidade//500)
		print(valor)
	elif(ingrediente == "CENOURA"):
		valor = (quantidade//100)
		print(valor)
	elif(ingrediente == "KAMPYO"):
		valor = (quantidade//20)
		print(valor)
	elif(ingrediente == "NORI"):
		valor = (quantidade//50)
		print(valor)
	elif(ingrediente == "OMELETE"):
		valor = (quantidade//200)
		print(valor)
	elif(ingrediente == "PEPINO"):
		valor = (quantidade//150)
		print(valor)
	elif(ingrediente == "SALMAO"):
		valor = (quantidade//300)
		print(valor)
	elif(ingrediente == "SHITAKE"):
		valor = (quantidade//150)
		print(valor)
else:
	print("Entrada invalida")
		