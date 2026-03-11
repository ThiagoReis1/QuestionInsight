nascimento = int(input("nascimento: "))
pais = input("B ou E: ")
idade = 2023 - nascimento

if (pais == "E" and idade >= 16):
	print("sim")
	idade = (2023 - nascimento) - 16
	print(idade)
	
elif (pais == "B" and idade >= 18):
	print("sim")
	idade = (2023 - nascimento) - 18
	print(idade)
	
elif (pais == "B" and idade < 18):
	print("nao")
	idade = 18 - (2023 - nascimento)
	print(idade)
elif (pais == "E" and idade < 16):
	print("nao")
	idade = 16 - (2023 - nascimento)
	print(idade)
else:
	print("invalido")
	