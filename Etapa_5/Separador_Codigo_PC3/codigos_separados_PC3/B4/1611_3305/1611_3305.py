from numpy import*

etiquetas = input("Entre com a string:")
i = 0
custo = 0
while(i<len(etiquetas)):
	if(etiquetas[i] == "A"):
		custo = custo + 0.15
	elif(etiquetas[i] == "E"):
		custo = custo + 0.15
	elif(etiquetas[i] == "I"):
		custo = custo + 0.15
	elif(etiquetas[i] == "O"):
		custo = custo + 0.15
	elif(etiquetas[i] == "U"):
		custo = custo + 0.15
		print(round(custo,2))
	else:
		custo = custo + 0.17
print(round(custo,2))
