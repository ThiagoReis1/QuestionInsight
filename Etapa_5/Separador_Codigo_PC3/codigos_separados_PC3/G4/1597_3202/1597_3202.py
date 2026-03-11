from numpy import*
v = array(eval(input()))
for i in range(size(v)):
	if (v[i]>80):
		x= sum(v) - 5
	else:
		x = sum(v)
print(round(x,2))