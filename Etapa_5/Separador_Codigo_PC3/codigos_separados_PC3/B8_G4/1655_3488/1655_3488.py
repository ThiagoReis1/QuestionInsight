from numpy import*

a = input("").split(',')

z = zeros(5, dtype=int)
b = 0
c = 0
d = 0
e = 0
f = 0


for i in range(size(a)):
	if(a[i] == "AC"):
		b = b + 1
	elif(a[i] == "AM"):
		c = c + 1
	elif(a[i] == "PA"):
		d = d + 1
	elif(a[i] == "RO"):
		e = e + 1
	elif(a[i] == "RR"):
		f = f + 1
		
z[0] = b
z[1] = c
z[2] = d
z[3] = e
z[4] = f

print(max(z))
print(z)