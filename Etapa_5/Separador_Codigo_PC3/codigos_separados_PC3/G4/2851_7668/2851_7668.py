from numpy import*
v=array(eval(input("")))
j=0
for i in range(size(v)):
	j=j+v[i]
	if(v[i]==99):
		j=(j-99)*2
print(j)