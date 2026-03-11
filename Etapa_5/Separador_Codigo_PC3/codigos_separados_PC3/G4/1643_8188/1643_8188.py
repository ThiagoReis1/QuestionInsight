from numpy import*

nota=array(eval(input("digite ")))
cont=0
a=0

for i in range(size(nota)):
	if(nota[i] >= 5):
		cont=cont +1
print(cont)

v=zeros(cont,dtype=int)

for i in range(size(nota)):
	if(nota[i] >= 5):
		v[a]=i
		a=a+1
print(v)
	

	