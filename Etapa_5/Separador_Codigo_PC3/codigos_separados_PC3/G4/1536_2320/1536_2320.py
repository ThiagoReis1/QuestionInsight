x = int(input("X: "))
k = int(input("N ELEMENTOS: "))
from math import *
n = 0
e = 0
while n < k:
	e = e + (pow(x, n+1)/(n+1))*-1**n
	n = n + 1
if(k > 1):
	e = e - 1
print (round(e,8))