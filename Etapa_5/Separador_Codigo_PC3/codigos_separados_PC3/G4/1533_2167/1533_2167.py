from math import *
x = float(input())
k = int(input())
i = 1
coss = 1

while(x>0) and (k > i):
	coss = coss + (x **(2*i)/factorial(i*2))
	i = i + 1
print(round(coss, 8))