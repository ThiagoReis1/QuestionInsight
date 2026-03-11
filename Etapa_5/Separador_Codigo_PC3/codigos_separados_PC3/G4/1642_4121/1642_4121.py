from numpy import *
from numpy.linalg import *
tur=array(eval(input()))
t = 0
for ele in tur:
	if ele%5 == 0:
		t = t + 1
z= zeros(t,dtype=int)
t1 = 0
for i in range(len(tur)):
	if(tur[i]%5 == 0):
		z[t1]=i
		t1 = t1 + 1
print(t)
print(z)
	


	
	