from math import*
x = float(input("numx: "))
k = int(input("numk: "))
c = 0
s = 0
while(s>x):
	s = s+x**(2*c)/factorial(2*c)
	c = c+1
print(round(s,8))
	