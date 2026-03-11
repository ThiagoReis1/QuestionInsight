ano_nascimento = int(input())
pais_de_origem = input().upper()
arbitro = (2023 - ano_nascimento)
#mano que complicação toda foi essa???
if pais_de_origem == "B":
	if arbitro >= 21:
		print("sim")
		print(round(arbitro - 21, 2))
	elif arbitro < 21:
		print("nao")
		print(round(21 - arbitro, 2))
elif pais_de_origem == "C":
	if arbitro >= 24:
		print("sim")
		print(round(arbitro - 24, 2))
	elif arbitro < 24:
		print("nao")
		print(round(24 - arbitro, 2))
else:
	print("invalido")