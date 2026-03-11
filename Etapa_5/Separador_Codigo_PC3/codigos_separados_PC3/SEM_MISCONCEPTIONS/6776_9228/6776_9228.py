ano = int(input("ano de nascimento:"))
pais = input("pais: B para Brasil ou R para Reino Unido")

idade = 2023 - ano

if pais.upper() != "B" and pais.upper() != "R":
	print("invalido")

elif idade >= 17 and pais.upper() == "R":
	print("sim")
	print(idade - 17)
elif idade >= 18 and pais.upper() == "B":
	print("sim")
	print(idade - 18)
elif idade < 17 and pais.upper() == "R":
	print("nao")
	print(17 - idade)
else:
	print("nao")
	print(18 - idade)