from math import * 

x = float(input())
k = int(input())

i = 0
total = 0

while (i < k):
	s = (-1)**i*(x**(2*i + 1))/(factorial(2*i + 1))
	total = total + s
	i = i + 1
	
print(round(total,9))