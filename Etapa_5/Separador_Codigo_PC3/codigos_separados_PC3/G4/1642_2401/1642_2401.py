from numpy import*
vetor=array(eval(input(" ")))
i=0
a=0
j=0
z=0
while(i<size(vetor)):
	if(vetor[i]%5 == 0):
		a=a+1
	i=i+1
v=zeros(a, dtype= int)
while(j<size(vetor)):
	if(vetor[j]%5 == 0):
		v[z]=j
		z=z+1
	j=j+1
print(a)
print(v)