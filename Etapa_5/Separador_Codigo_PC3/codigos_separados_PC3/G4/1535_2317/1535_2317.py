x = int(input("X:"))
k = int(input("N elementos:"))
from math import*
n = 0
e = x
j = -1 
while n < k:
	e = e + (pow(x, n+2)/ (n+2))*j
	j = j*(-1)
	n = n + 1


print(round(e,6))