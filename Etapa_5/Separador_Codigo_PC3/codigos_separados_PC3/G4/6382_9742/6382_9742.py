from numpy import *

n = array(eval(input("N: ")))
x = zeros(size(n),dtype=int)

for i in range(size(n)):
	if n[i]==9:
		x[i]=0
	else:
		x[i]= (n[i]+1)**2
		
print(x)