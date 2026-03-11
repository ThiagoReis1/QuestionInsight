from numpy import*

s = input("string: ").split(',')

a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(size(s)):
	if(s[i] == "AC"):
		a = a + 1
	elif(s[i] == "AM"):
		b = b + 1
	elif(s[i] == "PA"):
		c = c + 1
	elif(s[i] == "RO"):
		d = d + 1
	elif(s[i] == "RR"):
		e = e + 1

v = zeros(5,dtype=int)
v[0] = a
v[1] = b
v[2] = c
v[3] = d
v[4] = e
print(max(v))
print(v)