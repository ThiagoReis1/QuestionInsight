from numpy import*
v = array(eval(input("Vec:")))
i = 0
a = size(v)
while (i<a):
	if (v[i]>=80.0):
		v[i]=v[i] - 5
	i += 1
print(round(sum(v),2))