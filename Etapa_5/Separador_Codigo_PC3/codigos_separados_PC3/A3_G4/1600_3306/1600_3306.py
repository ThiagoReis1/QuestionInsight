from numpy import*
v= array(eval(input("digite o vetor custo:")))
i=0
total= 0
desc= 85/100
soma= 0
while(i<size(v)):
	if(v[i]>80):
		total=total+(v[i]*desc)
	else:
		total=total + v[i]
	i=i+1

print(round(total, 2))
		