from numpy import *
x=array(eval(input()))
npar=0
for i in range(0, size(x)):
	if x [i] <70: 
		npar = npar + 1
print(npar)
aux=zeros(npar,dtype=int)
j=0
for i in range(0,size(x)):
	if x [i]<70:
		aux[j]=i
		j+=1
print(aux)

