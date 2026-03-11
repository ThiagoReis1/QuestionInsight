from numpy import *
v = array (eval(input ("vetor: ")))
npar = 0
for i in range (size(v)):
	if(v[i] % 2 == 0):
		npar=npar+1
co= zeros(npar,dtype=int)
x=0
for i in range (size(v)):
	if(v[i] % 2 == 0):
		co[x]=i
		x=x+1
	
print (npar)
print (co)

