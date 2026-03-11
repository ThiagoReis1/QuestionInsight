ano = int(input("ano: "))
pais = input("pais: ").upper()
idade = 2023 - ano

if idade >= 21 and pais == "B":
	caso = idade - 21
	print("sim")
	print(caso)
elif idade < 21 and pais == "B":
	caso = 21 - idade
	print("nao")
	print(caso)
elif idade >= 18 and pais == "R":
	caso = idade - 18
	print("sim")
	print(caso)
elif idade < 18 and pais == "R":
	caso = 18 - idade
	print("nao")
	print(caso)
else:
	print("invalido")