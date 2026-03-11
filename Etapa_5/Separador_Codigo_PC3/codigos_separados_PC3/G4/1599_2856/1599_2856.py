from numpy import*
v = array(eval(input("v: ")))
i = 0

while(i < size(v)):
	if(v[i] >= 80.0):
		v[i] = v[i] - (v[i] * 0.15)
	i = i + 1
	
x = sum(v)
print(round(x,2))