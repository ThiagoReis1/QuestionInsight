from numpy import *
turmas=array(eval(input()))
a=0
for j in turmas:
	if(j%5==0):
		a+=1
vetornovo=zeros(a,dtype=int)
c=0
for j in range(size(turmas)):
	if(turmas[j]%5==0):
		vetornovo[c]=j
		c+=1
print(a)
print(vetornovo)