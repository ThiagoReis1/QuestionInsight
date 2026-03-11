from math import *
n = int(input("n: "))
i = 0
while abs(n)!=n*(-1):
	if n>35 and n<95:
		i = i + 1
	n = int(input("n: "))
print(i)