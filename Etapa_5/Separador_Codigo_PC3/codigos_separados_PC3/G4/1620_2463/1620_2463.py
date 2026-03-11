from numpy import*

t=array(eval(input()))
p=array(eval(input()))
i=0
j=0
k=0
while(i<size(p)):
	x=(((p[j]*5)/100)*t[k])
	i=i+1
	j=j+1
	k=k+1
print(round(x, 2))