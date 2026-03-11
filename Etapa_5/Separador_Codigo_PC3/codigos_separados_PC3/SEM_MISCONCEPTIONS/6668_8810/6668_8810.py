from numpy import *

x = array(eval(input("Digite: ")))

aux = x[x > 170]

if size(aux) == 0:
	print(0.0)
	
else:
	resultado = sum(aux)/size(aux)
	print(round(resultado,2))
	

		
