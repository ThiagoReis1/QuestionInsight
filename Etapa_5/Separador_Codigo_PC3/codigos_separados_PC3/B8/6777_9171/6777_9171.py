ano = int(input("ano de nascimento: "))
pais = input("pais brasil(B), Inglaterra(I): ").upper()

if pais == "B" and ano <= 2005:
	idade = (2023 - ano) - 18
	print("sim")
	print(idade)
	
elif pais == "B" and ano > 2005:
	idade = (2023 - ano) - 18
	print("nao")
	print(idade*(-1))
	
elif pais == "I" and ano <= 2006:
	idade = (2023 - ano) - 17
	print("sim")
	print(idade)
	
elif pais == "I" and ano > 2006:
	idade = (2023 - ano) - 17
	print("nao")
	print(idade*(-1))
	
elif pais != "B" or pais != "I":
	print("invalido")