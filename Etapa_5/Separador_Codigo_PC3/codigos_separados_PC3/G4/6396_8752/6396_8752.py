from numpy import*

c = array(eval(input("")))

z = zeros(size(c),dtype = int)
e = 0

for i in range(size(c)):
	if c[e] == 0:
		z[e] = 0
	else:
		z[e] = c[e] * 2
	e = e + 1
print(z)		
		

	