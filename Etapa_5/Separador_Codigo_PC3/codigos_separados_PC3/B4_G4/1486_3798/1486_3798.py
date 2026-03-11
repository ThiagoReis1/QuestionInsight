nome=input("nome:").upper()
q=int(input("quantidade"))
if(q>0) and (q<10000):
	if(nome=="ARROZ"):
		x=q//500
	elif(nome=="CENOURA"):
		x=q//100
	elif(nome=="KAMPYO"):
		x=q//20
	elif(nome=="NORI"):
		x=q//50
	elif(nome=="OMELETE"):
		x=q//200
	elif(nome=="PEPINO"):
		x=q//150
	elif(nome=="SALMAO"):
		x=q//300
	elif(nome=="SHITAKE"):
		x=q//150
	else:
		print("Entrada invalida")
	print(x)
else:
	print("Entrada invalida")