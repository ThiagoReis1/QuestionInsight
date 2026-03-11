from numpy import*
v = array(eval(input("")))
n=0
for i in v:
	v[n] = v[n]** 2
	n = n + 1
print(v)