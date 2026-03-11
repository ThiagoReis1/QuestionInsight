from numpy import*

n=array(eval(input('')))

a=0
for i in range(size(n)):
	if (n[i] >= 5.0):
		a=a+1
cont=zeros(a, dtype=int)
i=0
for j in range(size(n)):
	if (n[j] >= 5.0):
		cont[i]+=j
		i+=1
print(a)
print(cont)
	
	