classificacao =  input("Classificacao da missao (A/B): ")
valor = float(input("Valor pago pela missao: "))

if (classificacao == "B".upper()):
	imposto = valor * 0.15
	vfinal = imposto - valor
	total = abs(vfinal)
	classe = "Chunin"
else:
	imposto = valor * 0.22
	vfinal = imposto - valor
	total = abs(vfinal)
	classe = "Jounin"
print("Classe: ", classe)
print(round(total,2))