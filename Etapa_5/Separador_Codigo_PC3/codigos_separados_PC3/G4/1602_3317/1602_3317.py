from numpy import*
from numpy.linalg import*
vt = array(eval(input("digite: ")))
ka = zeros(shape(vt)[0], dtype=int)
for i in range(shape(vt)[0]):
	ka[i] = sum(vt[i,:])
for v in range(size(ka)):
	if(ka[v] == max(ka)):
		print(v+1)
