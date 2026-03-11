from numpy import *
notas = array(eval(input("notas: ")))
pesos = array([3,5,1])	  
num = notas * pesos 
				  
media = sum(num) / sum(pesos)
print(round(media, 2)) 
