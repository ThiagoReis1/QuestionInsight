ano_nascimento = int(input("digite o ano de nascimento: "))
pais = input("digite B ou I: ").upper()
ano = 2023 - ano_nascimento

if(ano >= 18 and pais == "B"):
	total = ano - 18
	print("sim")
	print(total)
elif(0 < ano < 18 and pais == "B"):
	total = 18 - ano
	print("nao")
	print(total)
elif(ano >= 17 and pais == "I"):
	total = ano - 17
	print("sim")
	print(total)
elif(0 < ano < 17 and pais == "I"):
	total = 17 - ano
	print("nao")
	print(total)
else:
	print("invalido")