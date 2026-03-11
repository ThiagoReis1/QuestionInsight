from numpy import*
v= array(eval(input()))
i=0
for x in range(size(v)):
	if v[x] < v[0]:
		i= i+1
		print(x)

print(i)