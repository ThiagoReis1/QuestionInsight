from numpy import*
from numpy.linalg import*

m = array(eval(input("")))
z = zeros(m.shape[0], dtype=float)

menor=0
posicao=0

for i in range (m.shape[0]):
	z[i]=min(m[i,:])
menor=min(z)
if(menor==z[0]):
	print(0)
elif(menor==z[1]):
	print(1)
elif(menor==z[2]):
	print(2)


