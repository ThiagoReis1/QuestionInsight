from numpy import *
a=array([BANANA,BIFE,FEIJOADA,OMELETE,TOMATE])
b=array([0.97,2.95,1.27,1.04,0.2])
b=b.T
i=0
while (i<size(a)):
	b=b+a[i]
	i=i+1	
print(round(b, 2))





