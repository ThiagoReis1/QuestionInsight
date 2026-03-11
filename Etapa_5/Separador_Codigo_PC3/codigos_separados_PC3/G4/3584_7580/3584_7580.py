from numpy import*
v = array(eval(input(': ')))
i =0 
while i < size(v):
	if v[i] > 200:
		v[i] -= v[i]*0.15 
	i += 1
print(round(sum(v),2))