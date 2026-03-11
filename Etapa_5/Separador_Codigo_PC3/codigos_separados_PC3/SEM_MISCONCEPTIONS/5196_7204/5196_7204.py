valor = float(input("valor antigo: "))

if valor <= 100 :
	atual = valor*1.05
	p = round(atual,2)
	print(p,"ryous")
	print("Aumento de 5 porcento")
else:
	atual = valor*1.15
	p = round(atual,2)
	print(p,"ryous")
	print("Aumento de 15 porcento")