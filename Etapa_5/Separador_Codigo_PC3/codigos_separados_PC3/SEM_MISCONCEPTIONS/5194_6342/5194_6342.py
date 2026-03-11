clas = input("Insira a classificacao da missao utilizando A ou B: ")
pag = float(input("O valor a ser pago pela missao: "))

if clas == "A":
	total = pag * 0.22
	total1 = pag - total
	print("Classe: Jounin")
	print(round(total1, 2))
	
if clas == "B":
	total = pag * 0.15
	total1 = pag - total
	print("Classe: Chunin")
	print(round(total1, 2))
	
	