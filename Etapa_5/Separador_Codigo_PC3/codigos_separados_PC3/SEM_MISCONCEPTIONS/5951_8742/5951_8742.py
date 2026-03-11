opcao = input("qual sua opcao (T/S): ")
if opcao.upper() == "T":
	comida = int(input("quantas tapiocas: ")) * 4.50
	acai = int(input("quantos acais: ")) * 12
	total = comida + acai
	print(total)
else:
	comida = int(input("quantos salgados: ")) * 5
	acai = int(input("quantos acais: ")) * 12
	total = comida + acai
	print(total)