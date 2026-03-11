from numpy import*
v=array(eval(input("")), dtype=float)
a=min(v)
b=max(v)
c=(0.85 * a) + (0.15 *b)
d=(0.4 *a) + (0.6 * b)

x=array(zeros(2, dtype=int))
for i in range(size(v)):
	if ((v[i] >= a) and (v[i] < c)):
		x[0]=x[0]+1
	elif ((v[i] >=d) and (v[i] < b)):
		x[1]=x[1]+1
print(x)