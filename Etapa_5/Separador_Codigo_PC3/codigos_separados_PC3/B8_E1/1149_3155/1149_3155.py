regiao = input("Mensagem: ")
if(regiao == "Ponta Tempestade" or regiao == "Ilha do Dragao" or regiao == "Campina" or regiao == "Winterfell" or regiao == "Rochedo Casterly" or regiao == "Pyke" or regiao == "Correrio" or regiao == "Ninho da Aguia" or regiao == "Dorne"):
	if(regiao =="Ponta Tempestade"):
		print("Baratheon")
	elif(regiao == "Ilha do dragao"):
		print("Targaryen")
	elif(regiao == "Campina"):
		print("Tyrell")
	elif(regiao == "Winterfell"):
		print("Stark")
	elif(regiao == "Rochedo Casterly"):
		print("Lannister")
	elif(regiao == "Pyke"):
		print("Greyjoy")
	elif(regiao == "Correrio"):
		print("Tully")
	elif(regiao == "Ninho da Aguia"):
		print("Arryn")
	elif(regiao == "Dorne"):
		print("Martell")
else:
	print("Entrada", regiao, "invalida")
	
idade = int(input("Idade: "))
peso = float(input("Peso: "))
print("Entradas:",idade, "anos e", peso, "kg")
if(idade > 0 and idade < 130 and peso > 0.0 and peso < 550.0):
	if(idade <= 20 and peso <= 60):
		z = "9"
		print("Grupo de risco:", z)
	elif(idade <= 20 and (peso > 60 and peso <= 90)):
		z = "8"
		print("Grupo de risco:", z)
	elif(idade <= 20 and peso > 90):
		z = "7"
		print("Grupo de risco:", z)
	elif((idade > 20 and idade <= 50) and peso < 60):
		z = "6"
		print("Grupo de risco:", z)
	elif((idade > 20 and idade <= 50) and (peso > 60 and peso <= 90)):
		z = "5"
		print("Grupo de risco:", z)
	elif((idade > 20 and idade <= 50) and peso > 90):
		z = "4"
		print("Grupo de risco:", z)
	elif(idade > 50 and peso < 60):
		z = "3"
		print("Grupo de risco:", z)
	elif(idade > 50 and peso > 60 and peso <= 90):
		z = "2"
		print("Grupo de risco:", z)
	elif(idade > 50 and peso > 90):
		z = "1"
		print("Grupo de risco:", z)
else:
	print("Dados invalidos")