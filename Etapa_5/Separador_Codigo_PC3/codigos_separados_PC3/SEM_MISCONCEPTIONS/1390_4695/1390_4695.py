x = float(input("Digite o consumo: "))
taxa = 25
total1 = x*1.20
total2 = taxa+x*1.40
if(x<=100):
	print(round(total1,2))
else:
	print(round(total2,2))