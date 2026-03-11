produto = float(input(""))

if (produto <= 100): 
	total = produto + ((produto*5)/100)
	mensagem = "Aumento de 5 porcento"

else:
	total = produto + ((produto*15)/100)
	mensagem = "Aumento de 15 porcento"
	
print(round(total,2),"ryous")
print(mensagem)