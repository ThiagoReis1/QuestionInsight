classe = input("Digite a classificacao da missao (A ou B): " ).upper()
valormis = float(input("Digite o valor pago pela missao: "))

if( classe == "B"):
	imposto = valormis - (valormis * 0.15)
	print("Classe: Chunin")
	print(round(imposto,2))
	
else:
	imposto = valormis - (valormis * 0.22)
	print("Classe: Jounin")
	print(round(imposto,2))
	