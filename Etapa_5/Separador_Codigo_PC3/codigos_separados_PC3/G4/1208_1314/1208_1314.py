from numpy import*
d=array(eval(input("qual a distancia:")))
i=0
k=0
while(i<size(d)):
	if(d[i]<98.48):
		k=k+1
	i=i+1
print("98.48")
print(k)