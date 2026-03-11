from numpy import*
v = array(eval(input("vetor compras: ")))

i = 0 

while(i < len(v)):
	if (v[i] > 80):
		v[i] = v[i] + (v[i]*15/100)
	else:
		v[i] = v[i]
	i = i + 1
s = sum(v)
print(round(s,2))