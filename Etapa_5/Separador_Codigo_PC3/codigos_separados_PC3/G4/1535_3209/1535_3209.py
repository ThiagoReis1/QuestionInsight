from math import *
x = float(input())
k = int(input())
cont = 1
acm = 0
pos = 0
while ( pos < k):
	y = ((-1) ** pos) *(x**cont)/ (cont)
	cont += 2
	pos += 1
	acm = acm + y
print(round(acm,6))