m = float(input("Digite o consumo: "))

if m <= 100:
	a= (1.2 * m)
	
else:
	a = ((m * 1.4) + 25)
print(round(a , 2))