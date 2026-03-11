unidade=input("Unidade ")
medida=float(input("Valor "))
if(unidade=="K"):
	lb=medida*2.20462
	print(round(lb,2))
else:
	k=medida/2.20462
	print(round(k,2))