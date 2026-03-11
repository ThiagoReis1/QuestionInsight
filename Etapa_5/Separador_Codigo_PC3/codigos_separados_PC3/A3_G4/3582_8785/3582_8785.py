from numpy import*

v= array(eval(input(': ' )))
s=0
for i in range(sum(v)):
	if v[i] >= 160:
		nv[i]= v - 25
	else:
		nv[i]= v
print(round(nv,2))