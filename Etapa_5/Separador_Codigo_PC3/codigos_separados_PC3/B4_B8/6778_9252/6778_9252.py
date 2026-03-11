ano = int(input("nascimento: "))

pais = input("Pais: ").upper()

idade = 2023 - ano

if(idade >=21 and pais == "B"):
	print("sim")
	print(idade - 21)
elif(idade>=20 and pais == "J"):
	print("sim")
	print(idade - 21)
elif(idade < 21 and pais == "B"):
	print("nao")
	print(21 - idade)
elif(idade < 20 and pais == "J"):
	print("nao")
	print(20-idade)
elif(pais != "B" or pais != "J"):
	print("invalido")
	

	
	

