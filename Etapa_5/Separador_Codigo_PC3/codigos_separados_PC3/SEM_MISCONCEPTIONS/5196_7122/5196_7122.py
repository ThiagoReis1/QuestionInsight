p = float(input("Preco antigo: "))

if p <= 100.00:
	c = p + (p * (5/100))
	mensagem = "Aumento de 5 porcento"
else:
	c = p + (p * (15/100))
	mensagem = "Aumento de 15 porcento"
	
print(round(c,2),"ryous")
print(mensagem)