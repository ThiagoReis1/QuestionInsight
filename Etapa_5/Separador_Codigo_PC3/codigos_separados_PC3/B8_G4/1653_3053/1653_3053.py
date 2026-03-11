from numpy import*
a = input("Nacionalidades: ").split(',')
x = zeros(5, dtype=int)

b = 0
c = 0
d = 0
e = 0
f = 0

for i in range(len(a)):
	if (a[i] == "AR"):
		b = b + 1
		x[0] = b
	elif (a[i] == "BR"):
		c = c + 1
		x[1] = c
	elif (a[i] == "CL"):
		d = d + 1
		x[2] = d
	elif (a[i] == "CO"):
		e = e + 1
		x[3] = e
	elif (a[i] == "UY"):
		f = f + 1
		x[4] = f
		
M = max(x)
print(M)
print(x)
		
		
	