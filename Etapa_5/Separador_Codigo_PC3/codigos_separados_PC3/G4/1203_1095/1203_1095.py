from numpy import*
v=array(eval(input()))
i=0
j=0
print("2.5")
while i<size(v):
	if v[i]>2.5:
		j=j+1
	i=i+1
print(j)