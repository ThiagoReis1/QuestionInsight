from numpy import*
from numpy.linalg import*

matriz = array(eval(input()))

a  = shape(matriz)[0]
b = shape(matriz)[1]
c = zeros(a, dtype = int)
d = zeros(b, dtype = int)

for i in range(size(a)):
	x = min(a)
	for j in range(size(b))