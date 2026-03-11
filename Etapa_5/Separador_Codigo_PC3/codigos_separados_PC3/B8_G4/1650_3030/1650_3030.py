from numpy import*
from math import*
c = input("Qual a cor de cabelo?").upper()
cs = c.split(',')
p = 0
c = 0
r = 0
l = 0
b = 0
for i in range(len(cs)):
	if(cs[i] == "P"):
		p =p +1
	elif(cs[i] == "C"):
		c = c + 1
	elif(cs[i] == "R"):
		r = r + 1
	elif(cs[i] == "L"):
		l = l + 1
	elif(cs[i] == "B"):
		b = b + 1

z = zeros(5, dtype=int)
z[0] = p
z[1] = c
z[2] = r
z[3] = l
z[4] = b


m = max(z)
print(m)
print(z)