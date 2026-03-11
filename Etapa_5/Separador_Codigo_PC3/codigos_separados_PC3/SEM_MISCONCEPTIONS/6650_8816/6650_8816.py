from numpy import*

nota = array(eval(input("")))
peso = array([4,3])

				
total = ( (nota[0] * peso[0]) + (nota[1] * peso[1]) ) / (sum(peso))
				 
print(round(total,2))