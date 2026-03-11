from numpy import*
v=array(eval(input("vetor:")))

i=0
cont=0
x=0

while(i<size(v)):
	if(v[i]>80):
		x=x+5
		y=sum(v)-x
		cont=cont+1
	i=i+1
	
print(round(y,2))