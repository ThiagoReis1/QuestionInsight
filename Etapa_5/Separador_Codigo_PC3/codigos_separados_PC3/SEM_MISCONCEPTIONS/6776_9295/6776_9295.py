nascimento = int(input("Insira seu ano de nascimento: "))
pais = (input("Insira o pais: ")).upper()
ano = 2023
idade = ano - nascimento

if (idade >= 18) and (pais ==  "B"):
	apto = idade - 18
	print("sim")
	print(apto)
	
elif (idade >= 17) and (pais == "R"):
	apto = idade - 17
	print("sim")
	print(apto)
	
elif (idade < 17) and (pais == "R"):
	apto = 17 - idade
	print("nao")
	print(apto)
	
elif (idade < 18) and (pais == "B"):
	apto = 18 - idade
	print("nao")
	print(apto)
	
else:
	print("invalido")
	

