from numpy import*
v = array(eval(input("v: ")))
i = 0
while(i<size(v)):
	if(v[i]>80):
		v[i] = v[i]-5
	i = i + 1
m = sum(v)
print(round(m,2))
