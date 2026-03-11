idade = int(input("Digite sua idade:"))
peso = float(input("Digite seu peso:"))

if((idade>=0) and (idade<=20) and (peso>=0) and (peso<=60)):
	grupo = "9"
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Grupo de risco:",grupo)
elif((idade>=0) and (idade<=20) and (peso>=0) and (peso>60 and peso<=90)):
	grupo = "8"
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Grupo de risco:",grupo)
elif((idade>=0) and (idade<=20) and (peso>=0) and (peso>90)):
	grupo = "7"
	print("Entradas:",idade,"anos e ",peso,"kg")
	print("Grupo de risco:",grupo)
elif((idade>=0) and (idade>20) and (idade<=50) and (peso>=0) and (peso<=60)):
	grupo = "6"
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Grupo de risco:",grupo)
elif((idade>=0) and (idade>20) and (idade<=50) and (peso>=0) and (peso>60) and (peso<=90)):
	grupo = "5"
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Grupo de risco:",grupo)
elif((idade>=0) and (idade>20) and (idade<=50) and (peso>=0) and (peso>90)):
	grupo = "4"
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Grupo de risco:",grupo)
elif((idade>=0) and (idade>50) and (peso>=0) and (peso<=60)):
	grupo = "3"
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Grupo de risco:",grupo)
elif((idade>=0) and (idade>50) and (peso>=0) and(peso>60) and (peso<=90)):
	grupo = "2"
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Grupo de risco:",grupo)
elif((idade>=0) and (idade>50) and (idade<=130) and (peso>=0) and (peso>90) and (peso<=550)):
	grupo = "1"
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Grupo de risco:",grupo)
else:
	print("Entradas:",idade,"anos e",peso,"kg")
	print("Dados invalidos")
	
	