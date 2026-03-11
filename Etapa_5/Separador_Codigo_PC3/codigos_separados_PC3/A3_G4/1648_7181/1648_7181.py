from numpy import *

al=array(eval(input("frequencia:  ")))
aux=zeros(size(al), dtype=int)
cont=0

for i in range(0, size(al)):
	if(al[i-1]<70):
		cont=cont+1
		
aux=zeros(cont, dtype=int)
j=0
a=0
for i in range(0, size(al)):
	if(al[i]<70):
		aux[j]=a
		j=j+1
		a=a+1
	else:
		a=a+1

print(cont)

print(aux)
