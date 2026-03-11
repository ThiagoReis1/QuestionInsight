from numpy import*
v=array(eval(input("vetor:")))

cont=0
for i in range(size(v)):
	if(v[i] > (v[0]*0.2)+v[0] and v[i]<(v[0]*0.5)+v[0]):
		cont=cont+1
print(cont)