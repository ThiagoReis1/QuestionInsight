x = float(input("x: "))
k = int(input("k: "))
from math import*
i=0
coshx=0
while i<=k-1:
	coshx = coshx + (x**(2*i))/(factorial(2*i))
	i=i+1
print(round(coshx,8))