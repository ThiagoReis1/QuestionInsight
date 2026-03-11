a = str(input("Digite a Unidade Academica dos estudantes: ")).upper()
cont = 0
while a != "X":
	if a == "FT":
		cont += 1
		a = str(input("Digite a Unidade Academica dos estudantes: ")).upper()
	else:
		a = str(input("Digite a Unidade Academica dos estudantes: ")).upper()
print(cont)