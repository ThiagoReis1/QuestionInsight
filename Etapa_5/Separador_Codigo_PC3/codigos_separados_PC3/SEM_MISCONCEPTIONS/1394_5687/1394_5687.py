quantdehoras = float(input("quantidade de horas: "))

if(quantdehoras <= 20 ): 
	tot = quantdehoras * 50
	print(round(tot, 1))
	
else: 
	tot2 = (20 * 50) + (quantdehoras - 20) * 70 
	print(round(tot2, 1))
	