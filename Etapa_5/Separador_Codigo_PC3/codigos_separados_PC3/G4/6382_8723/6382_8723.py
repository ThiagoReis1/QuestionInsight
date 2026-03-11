from numpy import*

k = array(eval(input("")))
z = zeros(size(k),dtype=int)
e = 0

for i in range(size(k)):
	if k[e] == 0:
		z[e] = 0 +1
		
	elif k[e] == 9:
		z[e]=0
	else:
		z[e] = k[e]+1
		z[e] = z[e]**2
	e = e +1
print(z)