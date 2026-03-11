nascimento = int(input("Ano de nascimento: "))
pais = input("Pais: ").upper()

idade = 2023 - nascimento

if idade >= 18 and pais == "B":
	print("sim")
	print(idade - 18)
elif idade >= 17 and pais == "I":
	print("sim")
	print(idade - 17)
elif idade < 18 and pais == "B":
	print("nao")
	print (18 - idade)
elif idade < 17 and pais == "I":
	print("nao")
	print(17 - idade)
else:
	print("invalido")
	
	
	
	