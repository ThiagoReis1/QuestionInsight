from math import*

x = float(input())
k = int(input())
j = 0
l = 0
		  
while (j < k):
	e = (x**j)/(factorial(j))
	l = l + e
	j = j + 1
		  
print(round(l , 9))		  