import math

x = float(input())
k = int(input())
a = 0

s = 0
so = 0

while(a < k):
	s = math.factorial(a)
	s = (x**a)/s
	so = so + s
	
	a = a + 1
	
print(round(so,9))