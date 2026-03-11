from numpy import *

notas = array(eval(input('qual valores das notas:')))
pesos = array([1, 3, 2, 5])
				  
num = notas * pesos
media = sum(num) / sum(pesos)
				  
print(round(media,2))