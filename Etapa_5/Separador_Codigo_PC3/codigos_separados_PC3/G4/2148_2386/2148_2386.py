from numpy import *
from math import *

#vetor com lados do poligono
va = array(eval(input()))

#acumulador
t = 0

#contas lados maiores ou iguas a 5
for a in range(0, size(va)):
	if(va[a]>=5):
		t = t + 1 
		

#resutados
print(sum(va))
print(t)



