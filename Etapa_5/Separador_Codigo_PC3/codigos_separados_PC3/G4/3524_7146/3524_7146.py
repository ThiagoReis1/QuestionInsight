x = float(input("x:"))
k = int(input("k:"))
i = 0

from math import*
while (k > 0):
	i = i + 2
	c = ((x ** i) / factorial(i)) 

x = float(input("x:"))

c_total = c * k
	
print(round(c_total, 8))
