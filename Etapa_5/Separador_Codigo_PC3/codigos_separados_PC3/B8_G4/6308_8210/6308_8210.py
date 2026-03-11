from numpy import*
v = input("v: ")

i = 0
a = 0
l = 0
p = 0
c1 = 0
c2 = 0
c3 = 0
while i < len(v):
	if v[i] == "A":
		a = a+16.75
		c1 = c1+1
	elif v[i] == "L":
		l = l+4.60
		c2 = c2+1
	elif v[i] == "P":
		p = p+2.85
		c3 = c3+1
	i=i+1
print(round((a+l+p),2),c1,c2,c3)