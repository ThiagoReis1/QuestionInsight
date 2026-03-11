from numpy import*
from numpy.linalg import*
v = array(eval(input("")))
i = 0
j = 0
menor = -1
ind=0
for i in range(shape(v)[0]):
	mt = min(v[i,:])
	if menor == -1:
		menor = mt
	else:
		if menor > mt:
			menor = mt
			ind=i
print(ind)
