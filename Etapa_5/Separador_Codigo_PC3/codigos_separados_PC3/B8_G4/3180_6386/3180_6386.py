from numpy import *
from numpy.linalg import *

m = array(eval(input("vetor: ")))

aux = zeros(4,dtype=int)

for i in range (size(m)):
	if m[i] == 1:
		aux[0] = aux[0] + 1
	elif m[i] == 2:
		aux[1] = aux[1] + 1
	elif m[i] == 3:
		aux[2] = aux[2] + 1
	elif m[i] == 4:
		aux[3] = aux[3] + 1
print(aux)