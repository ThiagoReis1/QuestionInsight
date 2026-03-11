from numpy import*
v= array(eval(input()))
i = 0

while (i < size(v)):
	if( v[i] == min(v)):
		v[i] = 0
	else:
		v[i] = v [i]
	i = i + 1
b = sum(v)/(size(v)-1)
print(round(b,2))