from math import*
ax = float(input())
k = int(input())
e = ax
j = 1
n = 3
cont = 1

while cont<k:
	j *= -1
	e = e + (((ax**(n))/n)*j)
	n += 2
	cont += 1
print(round(e,6))