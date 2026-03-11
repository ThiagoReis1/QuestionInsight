from numpy import*
v=array(eval(input("Vetor ")))
i=0
x=0
while(i<size(v) and v[i]<4):
	if(v[i]==1):
		x=x+80
	if(v[i]==2):
		x=x+40
	if(v[i]==3):
		x=x+20
	i=i+1
print(x)