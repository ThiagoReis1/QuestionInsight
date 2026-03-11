from numpy import *

n=array(eval(input("Notas: ")))

a=0
j=0


for i in range(size(n)):
	if n[i]>=5:
		a=a+1
print(a)
cont=zeros(a,dtype=int)
for i in range(size(n)):
	if n[i]>=5:
		cont[j]=i
		j=j+1
print(cont)




		
		
		
		
		
		
		
