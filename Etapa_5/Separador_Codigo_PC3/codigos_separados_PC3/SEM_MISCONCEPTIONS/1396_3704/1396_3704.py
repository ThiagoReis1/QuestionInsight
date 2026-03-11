valorCons = float(input("valor consumido:"))

a = (valorCons * 10/100)
b = (valorCons * 6/100)

if ( valorCons <= 300 ):

	print(round(valorCons + a, 2))
	
else :
	
	print(round(valorCons + b, 2))