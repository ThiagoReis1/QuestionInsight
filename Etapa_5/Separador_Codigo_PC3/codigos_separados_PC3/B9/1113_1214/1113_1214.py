#Universidade Federal do Amazonas
#Larissa Magno Leão
#21551610
#Exercicio 1

idade= int(input("Informe a idade:"))
peso= float(input("Informe o peso:"))

print("Entradas:",idade,"anos e",peso,"kg")

if (idade>0 and idade<130 and peso>0.0 and peso<550.0):
	if (idade<=20):
		if (peso<=60):
			grupo="9"
		elif(peso>60 and peso<=90):
			grupo="8"
		else:
			grupo="7"
	elif(idade>20 and idade<=50):
		if (peso<=60):
			grupo="6"
		elif(peso>60 and peso<=90):
			grupo="5"
		else:
			grupo="4"
	else:
		if (peso<=60):
			grupo="3"
		elif(peso>60 and peso<=90):
			grupo="2"
		else:
			grupo="1"
	print("Grupo de risco:",grupo)	
else:
	print("Dados invalidos")

	