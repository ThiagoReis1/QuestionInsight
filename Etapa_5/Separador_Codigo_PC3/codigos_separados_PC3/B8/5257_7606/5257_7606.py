p = float(input("qual o valor de venda"))
totalf = (total1 + total2 + total3 + total4)
if p<=50:
	total1 = p * 0.1
elif (p>50.01) and (p<=100):
	total2 = p * 0.5
elif (p>=100.01) and (p<=500):
	total3= p * 0.6
elif (p>500):
	total4= p * 0.7
	print(round(totalf, 2))
	
	
	
	
		
