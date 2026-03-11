from numpy import *

vetor = array(eval(input("Rony Rustico : ")))
acm = 0
cont = 0

for x in vetor :
	if x > 180 :
		acm = acm + x
		cont = cont + 1
		valor = acm / cont
if acm != 0 :
	print(round(valor,2))
else :
	print(0)