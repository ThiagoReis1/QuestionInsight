from math import*

x = float(input())
k = int(input())

i=0
e=0

while (i<k):
	e=(e+(x**i)/factorial(i))
	i=i+1
	
print(round(e,9))