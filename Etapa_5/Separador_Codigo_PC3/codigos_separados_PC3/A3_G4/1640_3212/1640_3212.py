from numpy import*
v=array(eval(input("vetor:")))

npar=0
for i in range(size(v)):
	if(v[i] % 2 != 0):
		npar=npar+1
		

k=0
f=0
d=zeros(npar, dtype=int)
for i in range(size(v)):
	if(v[i] % 2 != 0):
		k=k+1
		d=d+i
	
	
print(npar)
print(d)
		
	