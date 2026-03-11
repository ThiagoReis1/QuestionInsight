from numpy import*
v = array(eval(input()))
soma = (sum(v))
i = 0
d = 0
while(i<size(v)):
	if(v[i]>80):
		d = d + 1
	i = i + 1
c = sum(v) - 5*d
print(round(c,2))
