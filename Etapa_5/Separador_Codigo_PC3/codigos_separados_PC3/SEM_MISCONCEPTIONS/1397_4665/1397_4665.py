area = float(input("Qual o valor?"))
if(area<=10000):
	valor1 = area*5
	print(round(valor1,2))
else:
	valor2 = 10000*5+4*(area-10000)
	print(round(valor2,2))
	
