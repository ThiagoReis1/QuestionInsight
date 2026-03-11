ano = int(input("Entre com o ano de nascimento: "))
pais = input("Entre com B para nacionalidade brasileira e I para nacionalidade inglesa: ").upper()

idade = 2023 - ano
if pais != "B" and pais != "I":
	print("invalido")
	
if pais == "B" and idade < 18:
	print("nao")
	idade_falta = 18 - (idade)
	print(idade_falta)

elif pais == "I" and idade < 17:
	print("nao")
	idade_falta = 17 - (idade)
	print(idade_falta)

elif pais == "I" and idade >= 17:
	print("sim")
	idade_apta = (idade) - 17
	print(idade_apta)

elif pais == "B" and idade >= 18:
	print("sim")
	idade_apta = idade - 18
	print(idade_apta)
	


	
