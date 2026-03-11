from math import *

x = float(input())
k = int(input())
i = 0
cosseno = 0
while(i<k):
	cosseno = cosseno + (x**(2*i))/factorial(2*i)
	i+=1
print(round(cosseno, 8))
	