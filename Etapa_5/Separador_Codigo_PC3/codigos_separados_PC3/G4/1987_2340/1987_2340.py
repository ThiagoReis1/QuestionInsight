x = input("aminoacido: ").upper()
if(x == "alanina"): #C3 H7 N O2
	peso = ((3*12.011)+(7*1.00794)+(1400674)+(2*15.9994))
	print(round(peso,2))
elif(x == "valina"): #C5 H11 N O2
	peso = (5*12.011)+(11*1.00794)+(1400674)+(2*15.9994)
	print(round(peso,2))
elif(x == "tirosina"): #C9 H11 N O3
	peso = (9*12.011)+(11*1.00794)+(1400674)+(3*15.9994)
	print(round(peso,2))
else:
	print("Entrada:",x)
	print("Dado Invalido")