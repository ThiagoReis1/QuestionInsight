a=float(input("valor"))

if( a<= 300 ):
		  gorjeta=0.1*a
		  valor=a+gorjeta
		  print(round(valor,2))
else:
		  gorjeta=0.06*a
		  valor=a+gorjeta
		  print(round(valor,2))
		  