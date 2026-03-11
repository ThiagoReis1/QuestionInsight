nascimento = int(input("digite o ano de nascimento: "))
pais = input("digite o pais: ").upper()
situacao = 2023 - nascimento 

if (situacao >= 18) and (pais == "B"):
	total = situacao - 18
	print("sim")
	print(total)
elif (0 < situacao < 18) and (pais == "B"):
	total = 18 - situacao
	print("nao")
	print(total)
elif (situacao >= 17) and (pais == "R"):
	total = situacao - 17 
	print("sim")
	print(total)
elif (0 < situacao < 17) and (pais == "R"):
	total = 17 - situacao 
	print("nao")
	print(total)
else:
	print("invalido")