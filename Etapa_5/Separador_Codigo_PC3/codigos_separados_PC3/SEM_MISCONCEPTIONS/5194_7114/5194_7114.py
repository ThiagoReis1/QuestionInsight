clas = input("Digite a classificacao da missao A ou B: ")

if clas.upper() == "A":
	valor = float(input("Digite o valor pago pela missao: "))
	form1 = valor - (valor * 0.22)
	print("Classe: Jounin")
	print(round(form1, 2))
else:
	valor = float(input("Digite o valor pago pela missao: "))
	form2 = valor - (valor * 0.15)
	print("Classe: Chunin")
	print(round(form2, 2))