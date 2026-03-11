ano = int(input("Ano de nascimento: "))
pais = input("B/R: ")

idade = 2023 - ano
apto1 = idade - 18
apto2 = idade - 17
af1 = 18 - idade
af2 = 17 - idade

if pais.upper() == "B" and idade >= 18:
	print("sim")
	print(apto1)
	
elif pais.upper() == "B" and idade < 18:
	print("nao")
	print(af1)
	
elif pais.upper() == "R" and idade >= 17:
	print("sim")
	print(apto2)
	
elif pais.upper() == "R" and idade < 17:
	print("nao")
	print(af2)
	
else:
	print("invalido")
	
	

	
	
	