from numpy import*
s = input()
s = s.split(',')

a = 0
b = 0
c = 0
d = 0
e = 0

for i in s:
	if i == "AZ":
		a = a + 1
	elif i == "CA":
		b = b + 1
	elif i == "FL":
		c = c + 1
	elif i == "PA":
		d = d + 1
	else:
		e = e + 1

z = zeros(5,dtype= int)
z[0] = a
z[1] = b
z[2] = c
z[3] = d
z[4] = e

print(max(z))
print(z)