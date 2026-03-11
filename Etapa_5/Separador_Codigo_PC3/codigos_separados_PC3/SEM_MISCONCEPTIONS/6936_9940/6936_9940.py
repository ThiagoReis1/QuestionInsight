valor= float(input(" "))
opcao= input(" ").upper()

if opcao=="C":
	parcela= int(input(" "))
	if parcela==1:
		print(round(valor,2))
	
	else:
		print(round(valor+valor*(0.08),2))
		
else:
	x= valor-valor*0.13
	print(round(x,2))