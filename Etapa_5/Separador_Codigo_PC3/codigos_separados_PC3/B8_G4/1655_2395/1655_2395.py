from numpy import*
v = input("").split(',')
a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(size(v)):
	if(v[i]=="ac".upper()):
		a = a + 1
	elif(v[i]=="am".upper()):
		b = b + 1
	elif(v[i]=="pa".upper()):
		c = c + 1
	elif(v[i]=="ro".upper()):
		d = d + 1
	elif(v[i]=="rr".upper()):
		e = e + 1
p = max(a, b, c, d, e)
print(p)
z = zeros(5, dtype=int)
z[0] = a
z[1] = b
z[2] = c
z[3] = d
z[4] = e
print(z)	
	