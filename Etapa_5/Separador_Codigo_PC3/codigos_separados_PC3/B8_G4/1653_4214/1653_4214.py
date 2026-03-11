from numpy import *
from numpy.linalg import *

a = array(input().split(','))
a = a.T

c = zeros(5, dtype = int)

for i in range(size(a)):
	if(a[i] == "AR"):
		c[0] = c[0] + 1
		
	elif(a[i] == "BR"):
		c[1] = c[1] + 1
		
	elif(a[i] == "CL"):
		c[2] = c[2] + 1
	
	elif(a[i] == "CO"):
		c[3] = c[3] + 1
		
	elif(a[i] == "UY"):
		c[4] = c[4] + 1
		
print(max(c))
print(c)