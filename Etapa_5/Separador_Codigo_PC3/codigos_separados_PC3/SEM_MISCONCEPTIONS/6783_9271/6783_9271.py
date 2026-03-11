nascimento = int(input("Digite a data de nascimento: "))
pais = input("Digite o pais: ").upper()
idade = 2023 - nascimento
if pais == "B" and idade >= 18:
	aptidao = idade - 18
	print("sim")
	print(aptidao)
elif pais == "E" and idade >=16:
	aptidao = idade - 16
	print("sim")
	print(aptidao)
elif pais == "B" and idade < 18:
	aptidao = 18 - idade
	print("nao")
	print(aptidao)
elif pais == "E" and idade < 16:
	aptidao = 16 - idade
	print("nao")
	print(aptidao)
else:
	print("invalido")