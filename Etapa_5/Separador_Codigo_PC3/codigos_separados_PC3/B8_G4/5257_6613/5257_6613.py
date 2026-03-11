p = float(input("Preco de custo:"))

if (p>0) and (p<=50):
	pf = p + p*1
	print(round(pf,2))	
elif (p>50) and (p<=100):
	pf = p + p*0.5
	print(round(pf,2))	
elif (p>100) and (p<=500):
	pf = p + p*0.4
	print(round(pf,2))
elif (p>500):
	pf = p + p*0.3
	print(round(pf,2))
		
	