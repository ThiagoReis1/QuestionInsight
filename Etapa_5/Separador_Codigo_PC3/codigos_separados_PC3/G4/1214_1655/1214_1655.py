from numpy import*
v=array(eval(input()))
i=0
j=0
r=217
while i<size(v):
	if v[i]<r :
		j=j+1
	i=i+1
print(r)
print(j)