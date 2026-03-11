ano = int(input("ano de nascimento: "))
local = input("B ou E: ")

if local.upper() == "B" or local.upper() == "E":
	if ano <= 2005 and local.upper() == "E":
		tempo = 2005 - ano
		print("sim")
		print(tempo)
	elif ano <= 2002 and local.upper() == "B":
		tempo = 2002 - ano
		print("sim")
		print(tempo)
	elif ano > 2005 and local.upper() == "E":
		tempo = ano - 2005
		print("nao")
		print(tempo)
	elif ano > 2002 and local.upper() == "B":
		tempo =  ano - 2002
		print("nao")
		print(tempo)
else:
	print("invalido")
		