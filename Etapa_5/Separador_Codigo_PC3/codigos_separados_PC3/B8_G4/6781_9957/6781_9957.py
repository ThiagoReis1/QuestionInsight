nascimento = int(input())
pais = input()

#Brasil
if pais == "B" or "b":
	if (2023 - nascimento) >= 21:
		print("sim")
		Print((2023 - nascimento) -18)
	else:
		print("nao")
		nao1 = ((2023 - nascimento) - 21)* -1
		print(nao1)
		
#Estados Unidos
elif pais == "E" or "e":
	if (2023 - nascimento) >= 18:
		print("sim")
		print((2023 - nascimento) - 18)
	else:
		print("nao")
		nao = ((2023 - nascimento) - 18)* -1
		up(print(nao))
		

elif not pais == "B" or "E" or "b" or "e":
	print("invalido")
	