from numpy import *
a = input("insira a sequencia: ").split(',')
p = 0
c = 0
r = 0
l = 0
b = 0
for i in range(len(a)):
	if(a[i].upper() == "P"):
		p += 1
	elif(a[i].upper() == "C"):
		c += 1
	elif(a[i].upper() == "R"):
		r += 1
	elif(a[i].upper() == "L"):
		l += 1
	elif(a[i].upper() == "B"):
		b += 1
k = zeros(5, dtype = int)
k[0] = p
k[1] = c
k[2] = r
k[3] = l
k[4] = b
print(max(k))
print(k)