from numpy import *
saq=array(eval(input()))
a=0
for i in range(size(saq)):
	if saq[i]>=2000:
		a+=1
print(a)
aux = zeros(a,dtype=int)
l=0
for i in range(size(saq)):
	if saq[i]>=2000:
		aux[l]=i
		l+=1
print(aux)
