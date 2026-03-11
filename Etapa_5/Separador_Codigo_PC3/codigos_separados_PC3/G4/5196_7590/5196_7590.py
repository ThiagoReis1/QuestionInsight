pa = float(input("preco antigo: "))

x = 5/100
y = 15/100

if(pa<=100.00):
	ms = (pa * x) + pa
	print(round(ms,2),"ryous")
	print("Aumento de 5 porcento")
	
else: 
	ms = (pa * y) + pa
	print(round(ms,2),"ryous")
	print("Aumento de 15 porcento")
	
	
	