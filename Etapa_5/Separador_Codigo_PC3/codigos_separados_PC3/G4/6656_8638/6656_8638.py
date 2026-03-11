from numpy import *
nota = array(eval(input(":")))
pesos =[3,4,2,1,4,5]
med = nota*pesos
med2= sum(med)/sum(pesos)
print(round(med2, 2))