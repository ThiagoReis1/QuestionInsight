from numpy.linalg import *
from numpy import *

matriz = array(eval(input("")))
menor = shape(matriz)[0]
total = zeros(menor,dtype=float)
i=0
while( i != menor):
	total[i] = total [i] + min(matriz[i,:])
	i = i + 1

print(min(total))
