cidade = input("qual a cidade: ")
idade = int(input("idade: ")

if(idade > 13 and idade < 65):
	if(cidade == "Porto Velho"):
		Passagem = 500
		elif(cidade == "Santarem"):
			Passagem = 370
		elif(cidade = "Belem"):
			Passagem = 600
		elif(cidade = "Tefe"):
			Passagem = 360
		elif(cidade == "Tabatinga"):
			Passagem == 550
	if(idade <= 2):
	Pass = Passagem * 0
	elif(idade >=3 and <= 12):
	Pass = Passagem / 2
	elif(idade >= 65):
	Pass = Passagem = 0.30
		
		else:
		print("Entradas:", cidade , idade)
		print("entradas invalidas")
	else:
		print("Entradas:", cidade , idade)
		print("entradas invalidas")
else:
	print("Entradas:", cidade , idade)
	print("entradas invalidas")

print("Entradas:", cidade , idade)
print("Passagem:" , "R$" , Passagem)