a = float(input("numero de pizza encomendadas: "))

if(a<3):
	calculo = a*5.00+3.00
	print("total=", round(calculo))
elif(a==3):
	calculo = a*5.00+3.25
	print("total=", round(calculo,2))
elif (a>3):
	calculo = a*5.00+4.50
	print("total=",round(calculo,2))