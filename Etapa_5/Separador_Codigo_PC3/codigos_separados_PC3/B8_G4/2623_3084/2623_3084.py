from numpy import*
from numpy.linalg import*
x = array(eval(input()))
y = zeros(shape(x)[0])
i = 0
while(i<size(y)):
	y[i] = x[i,:].min()
	i = i + 1
if(y[0]<y[1] and y[0]<y[2]):
	z = 0
elif(y[1]<y[2] and y[1]<y[0]):
	z = 1
elif(y[2]<y[1] and y[2]<y[0]):
	z = 2
print(z)