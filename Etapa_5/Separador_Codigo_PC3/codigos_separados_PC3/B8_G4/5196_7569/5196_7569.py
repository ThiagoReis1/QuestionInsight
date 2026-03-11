a = float(input(": "))

if(a==1000):
	b = a*(15/100)
	print(round(b,2))
	print("Aumento de 15 porcento")
elif(a>1000):
	b = a*(5/100)
	print("Aumento de 5 porcento")