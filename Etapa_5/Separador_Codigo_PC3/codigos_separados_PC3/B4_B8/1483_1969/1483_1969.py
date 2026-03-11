nome = input("Nome do equipamento: ")
quantidade = int(input("Quantidade: "))

if(nome == "COMPUTADOR") :
	peso = 12
	print("Entrada invalida")
	
elif(nome == "FREEZER") :
	peso = 52
	
elif(nome == "FURADEIRA") :
	peso = 1.7
	
elif(nome == "LIQUIDIFICADOR") :
	peso = 1.8
	
elif(nome == "MICROONDAS") :
	peso = 15
	
elif(nome == "NOTEBOOK") :
	peso = 2.5
	
elif(nome == "TELEVISOR") :
	peso = 15
	
elif(nome == "VENTILADOR") :
	peso = 2.4
	
nome = peso * quantidade
print(round(nome, 2))