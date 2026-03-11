#Lucas Nascimento Estevam da Silva	Matricula: 21602757
#Trabalho Pratico 03		
#Exercicio 1

Nome = input("Nome do equipamento: ")
Cap = int(input("Capacidade de carga: "))

if(Cap < 0 or Cap > 1000 or (Nome != 'COMPUTADOR' and Nome != 'FREEZER' and Nome != 'FURADEIRA'and Nome != 'LIQUIDIFICADOR' and Nome != 'MICROONDAS' and Nome != 'NOTEBOOK' and Nome != 'TELEVISOR' and Nome != 'VENTILADOR')):
	print("Entrada invalida")

else:
	
	if(Nome == 'COMPUTADOR'):
		Peso = 12
	
	elif(Nome == 'FREEZER'):
		Peso = 52
	
	elif(Nome == 'FURADEIRA'):
		Peso = 1.7
	
	elif(Nome == 'LIQUIDIFICADOR'):
		Peso = 1.8
	
	elif(Nome == 'MICROONDAS'):
		Peso = 15
	
	elif(Nome == 'NOTEBOOK'):
		Peso = 2.5
	
	elif(Nome == 'TELEVISOR'):
		Peso = 15
	
	elif(Nome == 'VENTILADOR'):
		Peso = 2.4
	
	Quantidade = Cap // Peso
	print(int(Quantidade))


	
