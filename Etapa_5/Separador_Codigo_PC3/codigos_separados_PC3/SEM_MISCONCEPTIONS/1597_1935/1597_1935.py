from numpy import*

lista=array(eval(input("<3")))
s=sum(lista)
for e in range (0, size(lista)):
	if(lista[e]>80):
		s=s-5
print(round(s,2))