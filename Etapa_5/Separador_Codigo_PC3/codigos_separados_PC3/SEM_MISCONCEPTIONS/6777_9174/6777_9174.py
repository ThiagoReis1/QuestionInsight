ano = int(input("Digite ano: "))
pais = input("Digite pais: ").upper()

idade_min = 2023 - ano

if idade_min >= 18 and pais == "B":
	print("sim")
	apta = idade_min - 18
	print(apta)
elif idade_min < 18 and pais == "B":
	print("nao")
	tempo = 18 - idade_min
	print(tempo)
elif idade_min >= 17 and pais == "I":
	print("sim")
	apto = idade_min - 17
	print(apto)
elif idade_min < 17 and pais == "I":
	print("nao")
	apto = 17 - idade_min
	print(apto)
else:
	print("invalido")