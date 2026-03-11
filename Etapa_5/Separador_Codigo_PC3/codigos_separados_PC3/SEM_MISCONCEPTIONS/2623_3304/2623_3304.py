from numpy import*
from numpy.linalg import*

entrada = array(eval(input("")))

vz = zeros(shape(entrada)[0])

for i in range(shape(entrada)[0]):
	vz[i] = min(entrada[i,:])

for v in range(size(vz)):
	if(vz[v]==min(vz)):
		print(v)